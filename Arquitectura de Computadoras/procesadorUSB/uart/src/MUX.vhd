---------------------------------------------------------------------------------------------------
--
-- Title       : MUX
-- Design      : uart
-- Author      : Esau
-- Company     : WORKGROUP
--
---------------------------------------------------------------------------------------------------
--
-- File        : MUX.vhd
-- Generated   : Tue May 26 19:30:58 2015
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
--{entity {MUX} architecture {MUX}}

library IEEE;
use IEEE.STD_LOGIC_1164.all;



entity MUX is
	 port(
		 sel : in STD_LOGIC;
		 D1 : in STD_LOGIC_VECTOR(7 downto 0);
		 D0 : in STD_LOGIC_VECTOR(7 downto 0);
		 SALIDA : out STD_LOGIC_VECTOR(7 downto 0)
	     );
end MUX;

--}} End of automatically maintained section

architecture MUX of MUX is
begin

	-- enter your statements here --  
	SALIDA <= D1 when sel ='1' else D0;

end MUX;
