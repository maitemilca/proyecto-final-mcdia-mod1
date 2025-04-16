class MetadataManager:
    def __init__(self):
        self.data = {}

    def load_dataset(self, files):
        for sheet_name, register in files.items():
            self.data[sheet_name] = registers

    def list(self, sheet):
        return self.data.get(sheet, [])

    def insert(self, sheet, new_register):
        if sheet in self.data:
            self.data[sheet].append(new_register)
        else:
            self.data[sheet] = [new_register]

    def modify(self, sheet, index, field, new_value):
        if sheet in self.data and 0 <= index < len(self.data[sheet]):
            if field in self.data[sheet][index]:
                self.data[sheet][index][field] = new_value
                return True
        return False

    def delete(self, sheet, index):
        if sheet in self.data and 0 <= index < len(self.data[sheet]):
            self.data[sheet].pop(index)
            return True
        return False
