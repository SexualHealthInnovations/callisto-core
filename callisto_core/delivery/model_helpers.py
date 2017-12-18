import json

import gnupg


def gpg_encrypt_data(data, key):
    data_string = json.dumps(data)
    gpg = gnupg.GPG()
    imported_keys = gpg.import_keys(key)
    encrypted = gpg.encrypt(
        data_string,
        imported_keys.fingerprints[0],
        armor=True,
        always_trust=True)
    return encrypted.data


def _pop_answer_if_question_skips_eval(question, data):
    field_id = 'question_' + str(question['id'])
    if (
        question.get('skip_eval') and
        data.get(field_id)
    ):
        data.pop(field_id)
