entity priorityEncode is port (
    D: in bit_vector(0 to 3);
    X, Y, V: out bit);
end priorityEncode;

architecture Encode of priorityEncode is
signal xInt: bit;
begin
    x <= D(3) or D(2);
    xInt <= D(3) or D(2);
    y <= D(3) or (not D(2) and D(1));
    V <= xInt or D(1) or D(0);
end Encode;

