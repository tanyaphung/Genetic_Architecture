import random


def get_slim_outputs(directory, m):
    """
    This function obtains SLiM outputs. Each SLiM simulation is 100kb. The number of SLiM outputs to be obtained
    is dependent on the value of M. For example, if M is 200kb, 2 SLiM output files are obtained for analyses.
    :param directory: This is the directory where all of the SLiM outputs are stored
    :param m: This is the value of M in order to determine how many SLiM outputs to be obtained
    :return: The path of the SLiM outputs. For example, return the path "/u/flashscratch/flashscratch2/p/phung428/sim/
    for_inference/slim_output/return_503_EUR/return_503_EUR_200.slim".
    """
    # Step 1: Figure out how many SLiM outputs to obtain
    num_slim_outputs = int(float(m)/100000)

    # Step 2: Randomly generate num_SLiM_outputs numbers that ranges from 1 to 10000.
    # 100000 because I simulated 10000 SLiM simulations
    # NOTE: here, the range to draw from is hard-coded. This can be changed!
    rand_nums = random.sample(range(1, 10001), num_slim_outputs)

    # Step 3: Return the path
    filenames = []
    for i in rand_nums:
        filename = str(directory) + '/return_503_EUR_' + str(i) + '.slim'
        filenames.append(filename)

    return filenames
