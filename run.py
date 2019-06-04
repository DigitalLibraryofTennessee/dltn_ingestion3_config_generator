import yaml


class SetList:
    def __init__(self, sets_file):
        self.set_list = self.generate_setlist(sets_file)

    @staticmethod
    def generate_setlist(providers):
        data_sets = []
        for key, value in providers.items():
            for dataset in value:
                data_sets.append(dataset)
        return data_sets

    def generate_ingestion_3_config(self):
        with open('config.txt', 'w') as ingestion_config:
            ingestion_config.write('# Digital Library of Tennessee\n'
                                   'tn.provider = "Digital Library of Tennessee"\n'
                                   'tn.harvest.type = "oai"\n'
                                   'tn.harvest.endpoint = "http://dpla.lib.utk.edu:8080/repox/OAIHandler"\n'
                                   'tn.harvest.metadataPrefix = "MODS"\n'
                                   'tn.harvest.verb = "ListRecords"\n'
                                   'tn.harvest.setlist = "')
            position = 1
            for dataset in self.set_list:
                ingestion_config.write(f'{dataset}')
                if position != len(self.set_list):
                    ingestion_config.write(',')
                position += 1
            ingestion_config.write('"')
        return


if __name__ == "__main__":
    x = SetList(yaml.safe_load(open('sets.yml', 'r')))
    x.generate_ingestion_3_config()
