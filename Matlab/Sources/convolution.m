function T_conv = convolution(x,h)
    % Assertion: Ensure the x, h are nx1 vector

    % Use a temporary buffer to extend the length of convolution
    r = [x; zeros((length(h)-1),1)];
    % Create a teoplitz matrix
    c = [x(1); zeros(length(h)-1, 1)];
    toeplitzMat = toeplitz(c,r);
    % Compute
    T_conv = toeplitzMat' * h;
end

