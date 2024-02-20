from src.database.exams_database import ExamsDatabase


class ExamsBusiness(ExamsDatabase):

    def __init__(self):
        super().__init__()

    def findExamsAll(self):
        result = self.findExamsAll_db()

        datas = []
        for row in result:
            data = {
                "id": row.id,
                "name": row.name,
                "price": row.price,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }

            datas.append(data)

        return datas


if __name__ == "__main__":
    class_exams = ExamsBusiness()
    datas = class_exams.findExamsAll()
    print(datas)
