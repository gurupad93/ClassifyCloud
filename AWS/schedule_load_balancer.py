from decide_scaling import DecideScaling
from Metrics import Metrics


class ScheduleLoadBalancer(object):

    # schedule_load_balancer_task runs iteratively every 5 secs
    def schedule_load_balancer_task(self):

        msgs_in_queue = Metrics().get_messages_in_queue()
        num_workers = Metrics().get_number_workers()
        DecideScaling().decide_scaling(msgs_in_queue, num_workers)

