entity counter is port(
    UpDn, clk: In bit;
    Z: out bit;
    count: inout bit_vector(2 downto 0));
end counter;

Architecture count_arch of counter is
signal s, r: bit_vector(2 downto 0); 
begin
     s<= count;
     r<=s;
     process(clk)
     begin
     if UpDn = '1' then case s is 
         when "000"=>count<="010"; z<= '0';
         when "010"=>count<="110"; z<= '0';
         when "110"=>count<="001"; z<= '0';
         when "001"=>count<="011"; z<= '0';
         when "011"=>count<="111"; z<= '1';
         when "111"=>count<="000"; z<= '0';
     end case;
    end if;
     if UpDn = '0' then case s is 
        when "001"=>count<="011"; z<= '0';
         when "011"=>count<="101"; z<= '0';
         when "101"=>count<="111"; z<= '0';
         when "111"=>count<="000"; z<= '1';
         when "000"=>count<="010"; z<= '0';
         when "010"=>count<="100"; z<= '0';
         when "100"=>count<="110"; z<= '0';
         when "110"=> count <= "001"; z<='1';
     end case;
     end if;
    
    
    end process;
end count_arch;


    
