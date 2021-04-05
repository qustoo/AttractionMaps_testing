import datetime
import uuid
from dataclasses import dataclass

import pyqiwi

from data.config import QIWI_TOKEN, WALLET_QIWI, QIWI_PUBLIC_KEY

wallet = pyqiwi.Wallet(token=QIWI_TOKEN, number=WALLET_QIWI)


class NotEnoughMoney(Exception):
    pass


class NoPaymentFound(Exception):
    pass


@dataclass
class PaymentForQiwi:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())

    def check_payment(self):
        one_day_Ago = datetime.datetime.now() - datetime.timedelta(days=1)
        transactions = wallet.history(start_date=one_day_Ago).get("transactions")
        for transaction in transactions:
            if transaction.comment:
                if str(self.id) in transaction.comment:
                    if float(transaction.total.amount) >= float(self.amount):
                        return True
                    else:
                        raise NotEnoughMoney
        else:
            raise NoPaymentFound

    @property
    def invoice(self):
        link = "https://oplata.qiwi.com/create?publicKey={publicKey}&amount={amount}&comment={comment}"
        return link.format(publicKey=QIWI_PUBLIC_KEY, amount=self.amount, comment=self.id)
