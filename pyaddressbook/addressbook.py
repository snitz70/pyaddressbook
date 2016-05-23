import peewee as pw
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import pyaddressbook.ui_addressbook

#database = pw.SqliteDatabase('testing')
database = pw.MySQLDatabase('test', user='root', password='snitz086745')


class AddressbookDlg(QtWidgets.QDialog, pyaddressbook.ui_addressbook.Ui_Dialog):
    def __init__(self, parent= None):
        super(AddressbookDlg, self).__init__(parent)
        self.setupUi(self)
        mymodel = Addressbook.Model(addressbooks())
        self.address_comboBox.setModel(mymodel)
        contactmodel = Contact.Model(contacts(1))
        self.contact_listView.setModel(contactmodel)


class Model(QtCore.QAbstractTableModel):
    def __init__(self, _data):
        super(Model, self).__init__()
        self._data = _data

    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self._data)


class BaseModel(pw.Model):
    class Meta:
        database = database


class Addressbook(BaseModel):
    name = pw.CharField(unique=True)

    class Model(Model):
        def columnCount(self, index=QtCore.QModelIndex()):
            return 2

        def data(self, index, role=QtCore.Qt.DisplayRole):
            column = index.column()
            contact = self._data[index.row()]
            if role == QtCore.Qt.DisplayRole:
                return contact.name


class Contact(BaseModel):
    name = pw.CharField()
    address = pw.CharField(null=True)
    city = pw.CharField(null=True)
    state = pw.CharField(null=True)
    zipcode = pw.CharField(null=True)
    addressbook = pw.ForeignKeyField(Addressbook, related_name='contacts')

    class Model(Model):
        def columnCount(self, index=QtCore.QModelIndex()):
            return 2

        def data(self, index, role=QtCore.Qt.DisplayRole):
            column = index.column()
            contact = self._data[index.row()]
            if role == QtCore.Qt.DisplayRole:
                return contact.name


def create_tables():
    database.create_tables([Addressbook, Contact], True)


def create_addressbook(name):
    try:
        database.connect()
        with database.transaction():
            addressbook = Addressbook.create(name=name)
        database.close()
        return addressbook

    except pw.IntegrityError:
        raise


def addressbooks():
    database.connect()
    query = Addressbook.select()
    database.close()
    return query


def contacts(addressbook_id):
    database.connect()
    query = Contact.select().join(Addressbook).where(Contact.addressbook == addressbook_id)
    database.close()
    return query


def add_contact(addressbook_id, name):
    database.connect()
    with database.transaction():
        contact = Contact.create(addressbook=addressbook_id, name=name)
    database.close()
    return contact

if __name__ == '__main__':
    create_tables()
    app = QtWidgets.QApplication([])
    form = AddressbookDlg()
    form.show()
    app.exec_()
