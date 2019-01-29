from user_register.models import Account
import logging
import hashlib


# ユーザ登録モジュール
def user_register(id, password, email):
    pass_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()
    account = Account(id, pass_hash, email)
    success_check = False
    logger = logging.getLogger('development')
    logger.info('ユーザ登録トランザクション開始')
    try:
        account.save()
        success_check = True
        logger.info('ユーザ登録成功')
    except Exception as e:
        logger.info('ユーザ登録失敗')
        logger.error('=== エラー内容 ===')
        logger.error('type:' + str(type(e)))
        logger.error('args:' + str(e.args))
        logger.error('message:' + e.message)

    logger.info('ユーザ登録トランザクション終了')
    return success_check
