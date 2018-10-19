from decide_scaling import DecideScaling

class ScheduleLoadBalancer:

    # schedule_load_balancer_task runs iteratively every 5 secs
    def schedule_load_balancer_task(self):

        # get metrics
        DecideScaling.decide_scaling()



