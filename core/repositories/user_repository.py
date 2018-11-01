from core.models.user import User
from core.source.user_source import set_new_user, find_one_by_email, check_is_email_duplicate, get_id_by_email, \
    get_user_predictions, get_user_predictions_and_results
from werkzeug.security import check_password_hash
from core.source.snail_source import get_snail_name
from core.source.trainer_source import get_trainer_name
from core.source.round_source import get_open_round_id


class UserRepository:

    def register(self, first_name, last_name, email, password):
        user = User(first_name, last_name, email, password)
        return set_new_user(user)

    def check_is_email_duplicate(self, email):
        return check_is_email_duplicate(email)

    def login(self, user_email, user_password):
        user = find_one_by_email(user_email)

        if not user or not check_password_hash(user[3], user_password):
            return False

        return user

    def get_user_results(self, email):
        return self.get_predictions_from_db(email)

    def get_predictions(self, email):
        user_id = self.get_user_from_db(email)
        round_id = self.get_round_from_db()

        if user_id == "User Not In Database":
            return "User Not In Database"

        if not round_id:
            return_predictions = ["No Open Round"]
            return return_predictions

        predictions = self.get_predictions_from_db(user_id, round_id)
        return_predictions = []

        for prediction in predictions:
            snail = self.get_snail_name_from_db(prediction[1])
            trainer = self.get_trainer_name_from_db(snail[0][1])
            return_predictions.append([prediction[0], prediction[1], snail[0][0], trainer, round_id])

        return return_predictions

    def get_specific_round_predictions(self, user_email, round_id):
        predictions = self.get_predictions_from_db(get_id_by_email(user_email), round_id)

        return_predictions = []

        for prediction in predictions:
            snail = self.get_snail_name_from_db(prediction[1])
            trainer = self.get_trainer_name_from_db(snail[0][1])
            return_predictions.append([prediction[0], prediction[1], snail[0][0], trainer, round_id])

        return return_predictions

    def get_predictions_and_results(self, user_email, round_id):
        predictions = self.get_predictions_and_results_from_db(get_id_by_email(user_email), round_id)

        return_predictions = []

        for predictionResult in predictions:
            result_object = {}
            result_object["raceID"] = predictionResult[1]
            result_object["predictedID"] = predictionResult[3]
            result_object["predictedName"] = predictionResult[4]
            result_object["position"] = predictionResult[5]
            result_object["actualWinner"] = predictionResult[7]
            result_object["winnerTrainer"] = predictionResult[8]

            return_predictions.append(result_object)

        return return_predictions

    def get_user_from_db(self, email):
        return get_id_by_email(email)

    def get_round_from_db(self):
        return get_open_round_id()

    def get_predictions_from_db(self, user_id, round_id):
        return get_user_predictions(user_id, round_id)

    def get_snail_name_from_db(self, prediction):
        return get_snail_name(prediction)

    def get_trainer_name_from_db(self, snail):
        return get_trainer_name(snail)

    def get_predictions_and_results_from_db(self, user_id, round_id):
        return get_user_predictions_and_results(user_id, round_id)
