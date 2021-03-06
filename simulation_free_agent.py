from simulation import Simulation
import logging as log


class SimulationFreeAgent(Simulation):

    def __init__(self, stop_immediately_when_no_calls = False, number_agents=40, generate_history_file=True):
        Simulation.__init__(self, stop_immediately_when_no_calls, number_agents=number_agents, generate_history_file=generate_history_file)

        self._dial_level_recalc_period = Simulation.EPOCH


    def recalc_dial_level(self):
        """
        Ensure the number of in progress calls match the number of free agents
        """

        # Add up all the possible calls that could become available.
        in_progress = self.number_created_calls() + self.number_ringing_calls() + self.number_queued_calls()

        # Do we have excess agents?
        number_calls_to_make = self._number_free_agents - in_progress

        if number_calls_to_make < 0:
            number_calls_to_make = 0

        return number_calls_to_make

