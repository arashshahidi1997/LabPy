function plotDependencyGraph(dependencyGraph)
    nodes = keys(dependencyGraph);
    edges = [];
    weights = [];

    for i = 1:length(nodes)
        callees = dependencyGraph(nodes{i});
        for callee = callees
            edges = [edges; {nodes{i}, callee{1}}];
            weights = [weights; 1];  % Simple weight, can be complex based on further analysis
        end
    end

    G = digraph(edges(:,1), edges(:,2), weights);
    plot(G, 'Layout', 'force');
end
