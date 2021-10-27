function [W] = roof(w)
    assert(all(size(w) == [3,1]), "Variable w has to be a 3x1-vector!");
    %if(any(size(w) ~= [3,1]))
    %   error("Variable w has to be a 3x1-vector!"); 
    %end
    W = [0, -w(3), w(2); ...
         w(3), 0, -w(1); ...
         -w(2), w(1), 0]; ...
end

