import peewee as pw


database = pw.SqliteDatabase('testing')


class BaseModel(pw.Model):
    class Meta:
        database = database


class Addressbook(BaseModel):
    name = pw.CharField(unique=True)


class Contact(BaseModel):
    name = pw.CharField()
    address = pw.CharField()
    city = pw.CharField()
    state = pw.CharField()
    zipcode = pw.CharField()
    addressbook = pw.ForeignKeyField(Addressbook)


def create_tables():
    database.create_tables([Addressbook, Contact], True)


def create_addressbook(name):
    try:
        with database.transaction():
            addressbook = Addressbook.create(name=name)
        return addressbook

    except pw.IntegrityError:
        raise