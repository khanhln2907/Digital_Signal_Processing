function im_kron_rgb = merge_channels_kronecker(im)
cR = [ 1 0 1 ;   0.3 1 0;   0   0.3 1 ];
cG = [ 0 1 1 ;   0.3 0 1;   0.7 0.3 0 ];
cB = [ 0 0 0 ;   1   1 0;   0.7 1   0 ];

[row, col] = size(im);

channel = {cR, cG, cB};
imChan = cell(3,1);
for color = 1 : 3
    imki = zeros(row*3, col*3);
    for i = 0:2
       for j = 0:2
           thisChanColor = channel{color};
           imki(i*row+1:i*row+row, j*col+1: j*col+col) = thisChanColor(i+1,j+1) * im;
       end
    end
    imChan{color} = imki;
    %ref = kron(channel{color}, im);
end

im_kron_rgb = cat(3, imChan{1}, imChan{2}, imChan{3});
end