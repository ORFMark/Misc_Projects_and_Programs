-- The following is a STRUCTURAL VHDL description of the circuit of Figure 16-4
-- from Fundamentals of Logic Design, 5th ed.
-- Use the following command sequence to test this code converter:
-- force CLK 0 0, 1 100 -repeat 200
-- force X 0 0, 1 350, 0 550, 1 750, 0 950, 1 1350
-- run 1600

library BITLIB;
use BITLIB.bit_pack.all;

entity SM17_1 is
  port(X,CLK: in bit;
    Z: out bit);
end SM17_1;

architecture Structure of SM17_1 is
  signal A1,A2,A3,A5,A6,D3: bit:='0';
  signal Q1,Q2,Q3: bit:='0';
  signal Q1N,Q2N,Q3N, XN: bit:='1';
begin
  I1:  Inverter port map (X,XN);
  G1:  Nand3 port map (Q1,Q2,Q3,A1);
  G2:  Nand3 port map (Q1,Q3N,XN,A2);
  G3:  Nand3 port map (X,Q1N,Q2N,A3);
  G4:  Nand3 port map (A1,A2,A3,D3);
  FF1: DFF port map (Q2N,CLK,Q1,Q1N);
  FF2: DFF port map (Q1,CLK,Q2,Q2N);
  FF3: DFF port map (D3,CLK,Q3,Q3N);
  G5:  Nand2 port map (X,Q3,A5);
  G6:  Nand2 port map (XN,Q3N,A6);
  G7:  Nand2 port map (A5,A6,Z);
end Structure;
