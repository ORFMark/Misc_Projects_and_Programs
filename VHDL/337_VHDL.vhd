library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

Entity majority is 
port(
A: in std_logic_vector(3 downto 0);
O: out std_logic);
end majority;

Architecture majority_arch of majority is 
 begin
 O <= (A(1) and A(2) and A(3)) or (A(0) and((A(1) and A(2)) or (A(1) and A(3)) or (A(2) and A(3))));
end majority_arch;

