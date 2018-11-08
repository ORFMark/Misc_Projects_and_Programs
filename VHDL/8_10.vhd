entity book8_10 is port(
    x,y, clk: In bit;
    state: inout bit_vector(1 downto 0));
end book8_10a;

Architecture behavioral of Book8_10 is
signal s: bit_vector(1 downto 0);
begin
     s<=X&Y;
     process(clk)
     begin
     if s = "00" then case s is 
        when "00"=>state<="00";
        when "01"=>state<="10";
        when "10"=>state<="00";
        when "11"=>state<="10";
     end case;
      elsif s = "01" then case s is
        when "00"=>state<="00";
        when "01"=>state<="11";
        when "10"=>state<="00";
        when "11"=>state<="11";
     end case;
      elsif s = "10" then case s is
        when "00"=>state<="11";
        when "01"=>state<="10";
        when "10"=>state<="10";
        when "11"=>state<="00";
      end case;
      elsif s = "01" then case s is
        when "00"=>state<="11";
        when "01"=>state<="11";
        when "10"=>state<="11";
        when "11"=>state<="00";
     end case;
     end if;
    end process;
end behavioral;


    

