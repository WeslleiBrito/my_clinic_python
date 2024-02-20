from src.database.occupational_risks_database import OccupationalRisksDatabase


class OccupationalRisksBusiness(OccupationalRisksDatabase):

    def __init__(self):
        super().__init__()

    def findOccupationalRisksAll(self):
        result = self.findOccupationalRisksAll_db()

        datas = []
        for row in result:
            data = {
                "id": row.id,
                "name": row.name,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }

            datas.append(data)

        return datas


if __name__ == "__main__":
    class_occupational_risks = OccupationalRisksBusiness()
    datas = class_occupational_risks.findOccupationalRisksAll()
    print(datas)
