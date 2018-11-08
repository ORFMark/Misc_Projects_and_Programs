library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

Entity eGate is
Port(
  A,B,C,D,E: in std_logic;
  F        : out std_logic);
End eGate;

Architecture eGate_arch of eGate is
Begin
  F<= ((A or B) and (C or D)) and E;
End eGate_arch;

