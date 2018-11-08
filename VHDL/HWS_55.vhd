entity HWS_5_5 is port(
	x, clk: in bit;
	y: out bit:
	state: inout bit_vector(4 downto 0));
end HWS_5_5;

architecture Behavioral of HWS_5_5 is
constant a = '10000', b = '01000', c = '00100', d = '00010', e = '00001';
	begin
	process(clk)
	begin
		if x = '0' then case state is 
		begin
			when a=>state<=b;
			when b=>state<=c;
			when c=>state<=d;
			when d=>state<=e;
			when e=>state<=e;
			when others=>state<=a;
		end case;
		elsif x = '1' then case state is 
		begin
			when a=>state<=d;
			when b=>state<=c;
			when c=>state<=a;
			when d=>state<=b;
			when e=>state<=a;
			when others<=state=>a;
		end case;
		end if;
	end process;
	process(x, clk)
	begin
	if x = '0' then case state is 
		begin
			when a=>y<='0';
			when b=>y<='0';
			when c=>y<='0';
			when d=>y<='0';
			when e=>y<='0';
			when others=>y<='0';
		end case;
		elsif x = '1' then case state is 
		begin
			when a=>y<='0';
			when b=>y<='1';
			when c=>y<='1';
			when d=>y<='1';
			when e=>y<='1';
			when others<=y=>'1';
		end case;
		end if;
	end process;
end Behavioral;

	