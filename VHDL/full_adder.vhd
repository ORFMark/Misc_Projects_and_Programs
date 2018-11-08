library ieee;
use ieee.std_logic_1164.all;
entity full_adder is
  port (in1, in2, c_in : std_ulogic;
    sum, c_out : out std_ulogic);
end entity;

architecture dataflow of full_adder is
  signal s1,s2,s3 : std_ulogic;
  constant gate_delay : time := 5 ns;
begin
  l1: s1 <= (In1 xor In2) after gate_delay;
  L2: s2 <= (c_in and s1) after gate_delay;
  L3: s3 <= (In1 and In2) after gate_delay;
  L4: sum <= (s1 xor c_in) after gate_delay;
  L5: c_out <= (s2 or s3) after gate_delay;
end architecture;

library ieee;
use ieee.std_logic_1164.all;
entity testbench is
end testbench;

architecture functional of testbench is
  component full_adder is
    port (in1,in2,c_in : in std_ulogic;
    sum,c_out : out std_ulogic);
  end component;

  signal stim1,stim2,stim3 : std_ulogic;
  signal res1,res2 : std_ulogic;
begin
  stim1 <= '0', '1' after 50 ns, '0' after 100 ns, '1' after 150 ns, '0' after 200 ns,
    '1' after 250 ns, '0' after 300 ns, '1' after 350 ns, '0' after 400 ns;
  stim2 <= '0', '1' after 100 ns, '0' after 200 ns, '1' after 300 ns, '0' after 400 ns;
  stim3 <= '0', '1' after 200 ns, '0' after 400 ns;
  dut : full_adder port map (stim1,stim2,stim3,res1,res2);
end;

