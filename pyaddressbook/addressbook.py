import peewee as pw


database = pw.SqliteDatabase('testing')


class BaseModel(pw.Model):
    class Meta:
        database = database


class Addressbook(BaseModel):
    name = pw.CharField(unique=True)


def create_addressbook(name):
    try:
        with database.transaction():
            addressbook = Addressbook.create(name=name)
        return addressbook

    except pw.IntegrityError:
        raise