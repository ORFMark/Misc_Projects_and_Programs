entity XCLOR is port (
  X,Y: in bit;
  Z: out bit);
end XCLOR;

architecture Equation of XCLOR is
signal v, w: bit;
begin
    v <= not X and Y;
    w <= x and not y;
    z <= v or w;
end Equation; 
