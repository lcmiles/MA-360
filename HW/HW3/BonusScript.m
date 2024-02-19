%prompt use input
n = input('Enter the number of rows/colums: ');

%iterate over each row
for row = 1:n

    %print spaces
    for space = 1:(n - row)
        fprintf(' ');
    end
    
    %print '+'
    for plus = 1:row
        fprintf('+');
    end

    %print 'o'
    for o = 1:(n - row)
        fprintf('o');
    end

    fprintf('\n');
end