library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

Entity fGate is
Port(
  A,B,C,D,E: in std_logic;
  F        : out std_logic);
End fGate;

Architecture fGate_arch of fGate is
Begin
  F<= ((A XOR B) and (C or D));
End fGate_arch;

