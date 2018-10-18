from core.models.user import User
from core.source.user_source import set_new_user, find_one_by_email, email_is_duplicate, get_id_by_email, get_user_predictions
from werkzeug.security import check_password_hash
from core.source.snail_source import get_snail_name
from core.source.trainer_source import get_trainer_name
from core.source.round_source import get_round_id

class UserRepository:

    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        return set_new_user(user)

    def check_email(self, email):
        return email_is_duplicate(email)

    def login(self, user_email, user_password):
        user = find_one_by_email(user_email)

        if not user or not check_password_hash(user[3], user_password):
            return False

        return user

    def get_predictions(self, email):
        user_id = get_id_by_email(email)
        predictions = get_user_predictions(user_id)
        roundid = get_round_id()
        return_predictions = []


        for prediction in predictions:
            snail = get_snail_name(prediction[1])
            trainer = get_trainer_name(snail[0][1])
            return_predictions.append([prediction[0], prediction[1], snail[0][0], trainer, roundid])


        return return_predictions



