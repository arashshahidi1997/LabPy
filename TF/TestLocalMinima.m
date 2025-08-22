classdef TestLocalMinima < matlab.unittest.TestCase
    % Assumes LocalMinima.m is on MATLAB path.
    % Indices are 1-based (MATLAB).
    
    methods (Test)
        function test_basic_minima(testCase)
            x = [3 2 4 1 5 0 6];
            [M,V] = LocalMinima(x, [], [], []);  % no spacing, no threshold, all results
            testCase.verifyEqual(M(:), [2;4;6]);
            testCase.verifyEqual(V(:), [2;1;0]);
        end

        function test_spacing_pruning(testCase)
            x = [3 2 4 1 5 0 6];
            [M,V] = LocalMinima(x, 3, [], []);  % minima must be >=3 samples apart
            % Pairs (2,4) and then (4,6) are too close; larger value in each pair is removed.
            testCase.verifyEqual(M(:), [6]);
            testCase.verifyEqual(V(:), [0]);
        end

        function test_lessthan_filter(testCase)
            x = [3 2 4 1 5 0 6];
            [M,V] = LocalMinima(x, [], 1, []);  % only consider x < 1
            testCase.verifyEqual(M(:), [6]);
            testCase.verifyEqual(V(:), [0]);
        end

        function test_maxnumber_positive(testCase)
            x = [3 2 4 1 5 0 6];
            [M,V] = LocalMinima(x, [], [], 2);  % 2 smallest minima values
            % Smallest two minima values are 0@6 and 1@4
            testCase.verifyEqual(M(:), [6;4]);
            testCase.verifyEqual(V(:), [0;1]);
        end

        function test_maxnumber_negative(testCase)
            x = [3 2 4 1 5 0 6];
            [M,V] = LocalMinima(x, [], [], -2); % 2 largest minima values
            % Largest two minima values are 2@2 and 1@4
            testCase.verifyEqual(M(:), [2;4]);
            testCase.verifyEqual(V(:), [2;1]);
        end

        function test_padding_when_few_minima(testCase)
            x = [1 0 1]; % only one minimum at index 2
            [M,V] = LocalMinima(x, [], [], 3); % request 3 results => pad with NaN
            testCase.verifyTrue(isequaln(M(:), [2; NaN; NaN]));
            testCase.verifyTrue(isequaln(V(:), [0; NaN; NaN]));
        end

        function test_empty_input_returns_empty_or_nan(testCase)
            x = [];
            % No MaxNumberOfResults -> empty outputs
            [M1,V1] = LocalMinima(x, [], [], []);
            testCase.verifyEqual(numel(M1), 0);
            testCase.verifyEqual(numel(V1), 0);

            % With MaxNumberOfResults -> NaN padding
            [M2,V2] = LocalMinima(x, [], [], 2);
            testCase.verifyTrue(isequaln(M2(:), [NaN; NaN]));
            testCase.verifyTrue(isequaln(V2(:), [NaN; NaN]));
        end
    end
end
