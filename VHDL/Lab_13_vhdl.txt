library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ASR is
	port( clk: in STD_LOGIC;
		  Din: in STD_LOGIC;
		  data_valid: inout STD_LOGIC;
		  parity_error: out STD_LOGIC;
		  data: inout STD_LOGIC_VECTOR(3 downt 0);
		  strobe: out STD_LOGIC);
end ASR;

architecture ASRX of ASR is
	constant buad_rate: INTEGER :=550;
	constant end_count: INTEGER := 63*buad_rate;
	signal parity_bit: STD_LOGIC;
	signal timer: INTEGER range 0 to 63*buad_rate;
begin
	process(clk)
		begin
			if rising_edge(clk) then
				if(timer < end_count) then timer <= timer + 1;
				elsif Din = '1' then timer <= 0;
				endif;
				case timer is
					when 10* buad_rate => data_valid <='0';
						data(0) <= Din;
						strobe <= '1';
					when 11*buad_rate => strobe <= '0';
					when 18*buad_rate => data(1) <= Din;
							strobe <= '1';
					when 19*buad_rate => strobe <= '0';
					when 26*buad_rate => data(2) <= Din;
							strobe <= '1';
					when 27*buad_rate => strobe <= '0';
					when 34*buad_rate => data(3) <= Din;
							strobe <= '1';
					when 35*buad_rate => strobe <= '0';
					when 42*buad_rate => parity_bit <= Din;
							strobe <= '1';
					when 43*buad_rate => strobe <= '0';
					when others => NULL;
				end case;
			end if;
		end process;
	parity_error <= data_valid and (not parity_bit xor data(0) xor data(1) xor data(2) xor data(3));
end ASRX;
