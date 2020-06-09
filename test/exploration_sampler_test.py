import networkx as nx

#from littleballoffur.exploration_sampling import CommunityStructureExpansionSampler, CirculatedNeighborsRandomWalkSampler

from littleballoffur.exploration_sampling import LoopErasedRandomWalkSampler, BreadthFirstSearchSampler, DepthFirstSearchSampler
#from littleballoffur.exploration_sampling import RandomWalkSampler, RandomNodeNeighborSampler, MetropolisHastingsRandomWalkSampler
#from littleballoffur.exploration_sampling import ShortestPathSampler, CommonNeighborAwareRandomWalkSampler, NonBackTrackingRandomWalkSampler
#from littleballoffur.exploration_sampling import RandomWalkWithRestartSampler, RandomWalkWithJumpSampler, FrontierSampler, ForestFireSampler, SnowBallSampler


def test_loop_erased_random_walk_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = LoopErasedRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)

def test_breadth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = BreadthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)

def test_depth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = DepthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)