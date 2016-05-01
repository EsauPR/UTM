---------------------------------------------------------------------------------------------------
--
-- Title       : uart
-- Design      : uart
-- Author      : Esau
-- Company     : WORKGROUP
--
---------------------------------------------------------------------------------------------------
--
-- File        : uart.vhd
-- Generated   : Thu May  7 19:47:29 2015
-- From        : interface description file
-- By          : Itf2Vhdl ver. 1.20
--
---------------------------------------------------------------------------------------------------
--
-- Description : 
--
---------------------------------------------------------------------------------------------------

--{{ Section below this comment is automatically maintained
--   and may be overwritten
--{entity {uart} architecture {uart}}

library IEEE;
use IEEE.STD_LOGIC_1164.all;



entity uart is
	 port(
		 rxf : in STD_LOGIC;
		 txe : in STD_LOGIC;
		 rd_u : in STD_LOGIC;
--		 wr_u : in STD_LOGIC;
		 clk : in STD_LOGIC;
		 rst : in STD_LOGIC;
		 dataUSB : in STD_LOGIC_VECTOR(7 downto 0);
		 rd : out STD_LOGIC;
		 --wr : out STD_LOGIC;
--		 wr_ok : out STD_LOGIC;
		 da : out STD_LOGIC;
		 dato : out STD_LOGIC_VECTOR(7 downto 0)
	     );
end uart;

--}} End of automatically maintained section

architecture uart of uart is
begin
	
	process(clk)
	variable edo  : integer range 0 to 7;
	begin 		
		if falling_edge(clk) then
			if rst = '1' then
				dato <= "11111111";
				rd <= '1';
				da <= '0';
				edo := 0;
			else
				--dato <= "00000000";
				case edo is
					when 0 =>
						if rxf='0' then
							edo := edo+1;
						end if;
					when 1 =>
						rd <= '0';
						edo := edo +1;
					when 2 | 3 =>
						edo := edo+1;
					when 4 => 
						dato <= dataUSB;
						edo := edo+1;
					when 5 =>
						rd <= '1';
						da <= '1';
						edo := edo+1;
					when 6 =>
						if rd_u = '1' then
							da <= '0';
							edo := edo+1;
						end if;
					when others =>
						dato <= "01010101";
						edo := 0;
				end case;
				
			end if;		 
			
		end if;
	end process;

	 -- enter your statements here --

end uart;
