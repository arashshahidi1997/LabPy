function dependencyGraph = analyzeDependencies(folderPath)
    disp('preparing ...');
    files = dir(fullfile(folderPath, '*.m'));
    dependencyGraph = containers.Map('KeyType', 'char', 'ValueType', 'any');
    disp('entering loop');
    disp(length(files));
    for i = 1:length(files)
        disp(files(i).name);
        filename = fullfile(folderPath, files(i).name);
        content = fileread(filename);
        [folder, baseName, ext] = fileparts(filename);

        % Regular expression to find function calls
        calledFunctions = regexp(content, '[a-zA-Z0-9_]+\(', 'match');
        calledFunctions = unique(cellfun(@(x) x(1:end-1), calledFunctions, 'UniformOutput', false));

        % Remove any built-in or common functions or handle methods if necessary
        % Filter based on your project

        dependencyGraph(baseName) = calledFunctions;
    end
end
