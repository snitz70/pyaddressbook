import peewee as pw


database = pw.SqliteDatabase('testing')


class BaseModel(pw.Model):
    class Meta:
        database = database


class Addressbook(BaseModel):
    def __init__(self, name):
        super(Addressbook, self).__init__()
        self.name = name

    name = pw.CharField(unique=True)


