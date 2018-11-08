entity BitMag4 is port (
    A, B: in bit_vector(0 to 3);
    AltB, AeqB, AgtB: out bit);
end BitMag4;

architecture Compare of BitMag4 is 
    signal x: bit_vector(0 to 3);
    begin
        x(0) <= A(0) XNOR B(0);
        x(1) <= A(1) XNOR B(1);
        x(2) <= A(2) XNOR B(2);
        x(3) <= A(3) XNOR B(3);
        AeqB <= x(3) and x(2) and x(1) and x(0);
        AgtB <= (A(3) and not B(3)) or (x(3) and A(2) and not B(2)) or (x(3) and x(2) and a(1) and not B(1)) or (x(3) and x(2) and x(1) and A(0) and not B(0));
        AltB <= (B(3) and not A(3)) or (x(3) and B(2) and not A(2)) or (x(3) and x(2) and B(1) and not A(1)) or (x(3) and x(2) and x(1) and B(0) and not A(0));
end Compare;
