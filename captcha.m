function [output] = captcha()
output = zeros(5,1);
all_theta = load('all_theta.mat');
all_theta = cell2mat(struct2cell(all_theta))
output = predict(all_theta);
end


