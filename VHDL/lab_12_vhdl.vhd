library IEEE;
	use IEEE.STD_LOGIC_1164.all;
	use IEEE.STD_LOGIC_UNSIGNED.ALL;
	use IEEE.numeric_std.all;

entity BRM is
	Port( fast_clk: in STD_LOGIC;
	    reset: in STD_LOGIC;
	    enable: in STD_LOGIC; 
	    rate: in STD_LOGIC_VECTOR(7 downto 0);
	    carry: out STD_LOGIC; 
	    speed: in STD_LOGIC;
		brm_out, brm_led: out STD_LOGIC;
		q_out: out STD_LOGIC_VECTOR (7 downto 0);
		q_led: out STD_LOGIC_VECTOR(7 downto 0);
		SSEG_AN: out STD_LOGIC_VECTOR(3 downto 0) := "0000";
		SSEG_CA: out STD_LOGIC_VECTOR(6 downto 0) := "1111111"
		);
end BRM;

architecture BRM_Arch of BRM is
	constant clk_size: natural:=21;
	constant clk_delta: natural:=8;
	signal slow_clk: STD_LOGIC;
	signal cnt_Div: STD_LOGIC_VECTOR(clk_size downto 0);
	signal q: STD_LOGIC_VECTOR (7 downto 0);
	signal f: STD_LOGIC_VECTOR (7 downto 0);
	signal brm: STD_LOGIC;
begin
	process(fast_clk)
	begin
		if rising_edge(fast_clk) then
		cnt_Div <= cnt_Div + 1;
		end if;
	end process;
	slow_clk <= cnt_Div(clk_size) when speed = '0' else cnt_Div(clk_size-clk_delta);
	
	process(slow_clk, reset)
	begin
		if reset = '1' then q<="00000000";
		elsif rising_edge(slow_clk) then q <= q+1;
		end if;
	end process;

	f(0) <= '1' when 		   q="01111111";
	f(1) <= '1' when std_match(q,"-0111111");
	f(2) <= '1' when std_match(q,"--011111");
	f(3) <= '1' when std_match(q,"---01111");
	f(4) <= '1' when std_match(q,"----0111");
	f(5) <= '1' when std_match(q,"-----011");
	f(6) <= '1' when std_match(q,"------01");
	f(7) <= '1' when std_match(q,"-------0");
	brm <= '1' when 
	       (f and rate) /= "00000000" 
	       else '0';
	q_out<=q;
	q_led<=q;
	brm_out <= brm and slow_clk and not(enable);
	brm_led <= not(brm and slow_clk and not(enable));
	carry <= '1' when std_match(q,"11111111") else '0';
end brm_arch;
	
	