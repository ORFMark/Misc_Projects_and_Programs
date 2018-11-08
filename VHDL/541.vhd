entity counter is port(
    x_in, clk: In bit;
    y_out: out bit;
    state: inout bit_vector(2 downto 0));
end counter;

Architecture count_arch of counter is 
begin
     process(clk)
     begin
     if x_in = '1' then case s is 
         when "001"=>state<="100"; y_out<= '1';
         when "100"=>state<="011"; y_out<= '0';
         when "011"=>state<="010"; y_out<= '1';
         when "010"=>state<="000"; z<= '1';
         when "000"=>state<="100"; z<= '1';
         when "100"=>state<="011"; y_out<= '0';
		 when others=>state<="100"; y_out <= '1';
     end case;
    end if;
     if UpDn = '0' then case s is 
         when "001"=>state<="001"; y_out<= '0';
         when "100"=>state<="010"; y_out<= '0';
         when "101"=>state<="010"; y_out<= '0';
         when "000"=>state<="011"; y_out<= '0';
         when "010"=>state<="010"; y_out<= '0';
         when "000"=>state<="011"; y_out<= '0';
         when "011"=>state<="010"; y_out<= '0';
         when others=> state <= "000"; y_out<='0';
     end case;
     end if;
    
    
    end process;
end count_arch;


    
