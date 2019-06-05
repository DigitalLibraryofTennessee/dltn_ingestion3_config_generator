import yaml
from repox.repox import Repox


class SetList:
    def __init__(self, sets_file, repox_connection):
        self.set_list = self.generate_setlist(sets_file)
        self.bad_sets = self.check_setlist(repox_connection)

    @staticmethod
    def generate_setlist(providers):
        data_sets = []
        for key, value in providers.items():
            for dataset in value:
                data_sets.append(dataset)
        return data_sets

    def check_setlist(self, config):
        repox_connection = Repox(config['repox_base_url'], config['repox_username'], config['repox_password'])
        bad_sets = []
        for dataset in self.set_list:
            test = repox_connection.get_dataset_details(dataset)
            if 'result' in test:
                bad_sets.append(dataset)
        return bad_sets

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
    x = SetList(yaml.safe_load(open('sets.yml', 'r')), yaml.safe_load(open('config.yml', 'r')))
    if len(x.bad_sets) == 0:
        x.generate_ingestion_3_config()
        print('New config file generated.')
    else:
        print(f'These sets are bad: {x.bad_sets}')
