import sqlalchemy
from loguru import logger
from core.database import db
from core.constants import (RECORD_STILL_REFERENCED,
                            RECORD_NOT_DELETED, RECORD_DELETED)


class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(),
                           nullable=False)
    updated_at = db.Column(
        db.DateTime(timezone=True), default=db.func.current_timestamp(),
        nullable=False, onupdate=db.func.current_timestamp()
    )

    def create(self):
        try:
            db.session.add(self)
            is_saved, msg = self.save()
            if not is_saved:
                return False, msg
        except Exception as e:
            logger.exception(
                "Error creating object - {}. {}"
                    .format(self.__name__, str(e))
            )
            return False, None
        else:
            return self

    @classmethod
    def save(cls):
        try:
            db.session.commit()
            logger.debug('Successfully committed {} instance'
                             .format(cls.__name__))
        except sqlalchemy.exc.DBAPIError as e:
            msg = "Error code {}, {}".format(
                e.orig.pgcode, str(e.orig)
            )
            logger.exception(msg)
            return False, msg
        except Exception:
            logger.exception(
                'Exception occurred. Could not save {} instance.'.format(cls.__name__)
            )
            return False, None
        else:
            return cls, None

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except sqlalchemy.exc.InvalidRequestError:
            logger.warning(
                "Record is still referenced from table in {}"
                    .format(self)
            )
            return False, RECORD_STILL_REFERENCED
        except Exception as e:
            logger.exception(
                'Could not delete {} instance.'.format(self))
            return False, RECORD_NOT_DELETED
        else:
            return True, RECORD_DELETED
