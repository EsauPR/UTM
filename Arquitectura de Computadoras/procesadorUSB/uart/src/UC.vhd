	---------------------------------------------------------------------------------------------------
--
-- Title       : UC
-- Design      : uart
-- Author      : Esau
-- Company     : WORKGROUP
--
---------------------------------------------------------------------------------------------------
--
-- File        : UC.vhd
-- Generated   : Fri May  8 00:54:29 2015
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
--{entity {UC} architecture {UC}}

library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.STD_LOGIC_UNSIGNED.all;


entity UC is
	 port(
		 clk : in STD_LOGIC;
		 rst : in STD_LOGIC;
		 P_OK : in STD_LOGIC;
		 dato : out STD_LOGIC_VECTOR(15 downto 0);
		 PC : out STD_LOGIC_VECTOR(9 downto 0);
		 IR : in STD_LOGIC_VECTOR(15 downto 0)
	     );
end UC;

--}} End of automatically maintained section

architecture UC of UC is
signal C : integer range 0 to 50000001;
signal TPC : STD_LOGIC_VECTOR(9 downto 0);
signal seg : STD_LOGIC;
begin

C <= 0 when C = 50000000 else C + 1 when falling_edge( clk );
seg <= '1' when C = 49999999 else '0';

PC <= TPC;
--dato <= TPC(7 downto 0);

process (clk, rst)	
begin
	
	if rst = '1' then
			TPC <= "0000000000";
			
	elsif falling_edge( clk ) and seg = '1' then
		if P_OK = '0' then
			TPC <= TPC + 1;
			if TPC = 4 then
				TPC <= "0000000000";
			end if;

			dato <= IR(7 downto 0) & IR(15 downto 8);

		end if;
	end if;
end process;

end UC;
