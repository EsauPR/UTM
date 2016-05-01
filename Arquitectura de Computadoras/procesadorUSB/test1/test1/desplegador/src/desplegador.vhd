---------------------------------------------------------------------------------------------------
--
-- Title       : desplegador
-- Design      : desplegador
-- Author      : Esau
-- Company     : WORKGROUP
--
---------------------------------------------------------------------------------------------------
--
-- File        : desplegador.vhd
-- Generated   : Tue May 12 19:58:10 2015
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
--{entity {desplegador} architecture {desplegador}}

library IEEE;
use IEEE.STD_LOGIC_1164.all;



entity desplegador is
	 port(
		 da : in STD_LOGIC;
		 clk : in STD_LOGIC;
		 rd_u : out STD_LOGIC
	     );
end desplegador;

--}} End of automatically maintained section

architecture desplegador of desplegador is
signal C : integer range 0 to 50000001;
signal seg : STD_LOGIC;	  
signal tmp : STD_LOGIC;
begin								   
	
C <= 0 when C = 50000000 else C + 1 when falling_edge( clk );
seg <= '1' when C = 49999999 else '0';
	

	process( clk )
	begin
		if da = '1' then
			if seg = '1' then 
				rd_u <= '1';
			else
				rd_u <= '0';
			end if;
		end if;				
	end process;
	

end desplegador;
