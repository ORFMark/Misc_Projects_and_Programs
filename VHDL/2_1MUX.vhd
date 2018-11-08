entity MUX2_1 is port (
 S: in bit;
 I: in bit_vector(0 to 1);
 Y: out bit);
end MUX2_1;

architecture MUX of MUX2_1 is 
begin
    Y <= I(0) when S = '0' else I(1) when S = '1';
end MUX;


