# This class is responsible for creating and terminating instances
class DecideScaling(object):

    # decides scaling using scaling criteria formula
    # calls create_instances() or terminate_instances() or terminate_all_instances()
    def decide_scaling(self):
        pass

    # creates specified number of instances
    def create_instances(self, num_instances):
        pass

    # terminates specified number of instances
    def terminate_instances(self, num_instances):
        pass

    # terminate all instances
    def terminate_all_instances(self):
        pass
