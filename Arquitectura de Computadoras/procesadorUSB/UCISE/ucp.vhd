---------------------------------------------------------------------------------------------------
--
-- Title       : ucp
-- Design      : uart
-- Author      : Esau
-- Company     : WORKGROUP
--
---------------------------------------------------------------------------------------------------
--
-- File        : ucp.vhd
-- Generated   : Fri May  8 00:29:27 2015
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
--{entity {ucp} architecture {ucp}}

library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.STD_LOGIC_UNSIGNED.all;



entity ucp is
	 port(
		 DA : in STD_LOGIC;
		 clk : in STD_LOGIC;
		 rst : in STD_LOGIC;
		 datoRX : in STD_LOGIC_VECTOR(7 downto 0);
		 WR : out STD_LOGIC;
		 P_OK : out STD_LOGIC;
		 dato : out STD_LOGIC_VECTOR(7 downto 0);
		 RD : out STD_LOGIC;
		 dir : out STD_LOGIC_VECTOR(10 downto 0)
	     );
end ucp;

--}} End of automatically maintained section

architecture ucp of ucp is
signal TDA : STD_LOGIC;
signal TDato : STD_LOGIC_VECTOR(7 downto 0);
signal cont : STD_LOGIC_VECTOR(7 downto 0);
signal H : STD_LOGIC_VECTOR(7 downto 0);
signal Tdir : STD_LOGIC_VECTOR(10 downto 0);
begin

dir <= Tdir;	
	
process (clk)
variable edo : integer range 0 to 4;
variable edoWR : integer range 0 to 4;
begin
	if falling_edge( clk ) then
		if rst = '1' then
			edo := 0;
			WR <= '0';
			TDA <= '1';
			P_OK <= '1';
			edoWR := 0;
		else
			if TDA = '1' then
				if DA = '1' then
					TDA <= '0';
					TDato <= datoRX;
					RD <= '0';
				end if;
			else
				case edo is
					when 0 =>
						if TDato = "00000000" then
							edo := edo + 1;
							P_OK <= '0';
							--led1 <= '1';
						else
							edo := 0;
							P_OK <= '1';
							--led1 <= '0';
						end if;
						TDA <= '1';
					when 1 =>
						cont <= TDato;
						edo := edo + 1;
						TDA <= '1';
					when 2 =>
						H <= TDato;
						edo := edo + 1;
						TDA <= '1';
					when 3 =>
						Tdir <= H(2 downto 0) & TDato;
						edo := edo + 1;
						TDA <= '1';
					when 4 =>
						dato <= TDato;
						case edoWR is
							when 0 =>
								WR <= '1';
								edoWR := edoWR + 1;
								cont <= cont - 1;
							when 1 =>
								edoWR := edoWR + 1;
							when 2 =>
								WR <= '0';
								edoWR := edoWR + 1;
							when 3 =>
								Tdir <= Tdir + 1;
								edoWR := 0;
								TDA <= '1';
								if cont = 0 then
									edo := 0;
								end if;
							when others =>
								null;
						end case;
					when others =>
						null;
				end case;
			end if;
		end if;
	end if;
end process;
					
					
						
								
					

end ucp;
