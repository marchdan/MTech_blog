  
 f r o m   m i n g u s . c o r e   i m p o r t   *  
 f r o m   m i n g u s . c o n t a i n e r s   i m p o r t   *  
 # f r o m   m i n g u s . m i d i   i m p o r t   *  
 f r o m   m i n g u s . e x t r a   i m p o r t   *  
 f r o m   m i n g u s . m i d i   i m p o r t   *  
 f r o m   t i m e   i m p o r t   *  
 ' ' '  
 n o t e s . i s _ v a l i d _ n o t e ( n o t e )  
 n o t e s . r e d u c e _ a c c i d e n t a l s ( n o t e )  
 n o t e s . n o t e _ t o _ i n t ( n o t e )  
 n o t e s . i n t _ t o _ n o t e ( n o t e )  
 n o t e s . a u g m e n t ( n o t e )  
 n o t e s . d i m i n i s h ( n o t e )  
 n o t e s . t o _ m i n o r ( n o t e )  
 n o t e s . t o _ m a j o r ( n o t e )  
 ' ' '  
  
 d e f   t r a n s f o r m ( n o t e ) :  
 	 n o t e   =   n o t e . l o w e r ( ) . c a p i t a l i z e ( )  
 	 i f   n o t e s . i s _ v a l i d _ n o t e ( n o t e ) :  
 	 	 r e t u r n   n o t e  
 	 e l s e :  
 	 	 r a i s e   E x c e p t i o n ( " P l e a s e   e n t e r   a   v a l i d   m u s i c a l   n o t e :   "   +   n o t e )  
  
 d e f   t r a n s p o s e ( n o t e ,   t r a n s ) :  
 	 i f   t r a n s   >   0 :  
 	 	 f o r   i   i n   r a n g e ( t r a n s ) :  
 	 	 	 n o t e   =   n o t e s . a u g m e n t ( n o t e )  
 	 e l i f   t r a n s   <   0 :  
 	 	 t r a n s   =   t r a n s   *   - 1  
 	 	 f o r   i   i n   r a n g e ( t r a n s ) :  
 	 	 	 n o t e   =   n o t e s . d i m i n i s h ( n o t e )  
 	 r e t u r n   n o t e s . r e d u c e _ a c c i d e n t a l s ( n o t e )  
  
 d e f   g e t _ b a r ( t i m e ,   k e y ) :  
 	 b   =   B a r ( k e y ,   ( t i m e ,   4 ) )  
 	 r e t u r n   b  
  
 d e f   w r i t e m u s i c ( n t s ,   t i m e ,   k e y ,   i n s t ) :  
 	 t   =   T r a c k ( i n s t )  
 	 b t   =   0  
 	 b   =   g e t _ b a r ( t i m e ,   k e y )  
 	 f o r   i   i n   r a n g e ( l e n ( n t s ) ) :  
 	 	 b   +   N o t e ( n t s [ i ] )  
 	 	 i f   ( b t + 1 ) % t i m e   = =   0 :  
 	 	 	 t   +   b    
 	 	 	 b   =   g e t _ b a r ( t i m e ,   k e y )  
 	 	 b t   + =   1  
 	 # # t e s t   =   l i l y p o n d . f r o m _ T r a c k ( t )  
 	 # # l i l y p o n d . t o _ p d f ( t e s t ,   f i l e )  
 	 r e t u r n   t  
  
 i f   _ _ n a m e _ _   = =   " _ _ m a i n _ _ " :  
 	 c   =   C o m p o s i t i o n ( )  
 	 c h o i c e   =   i n t ( i n p u t ( " T r a n s p o s e ( 0 )   o r   W r i t e ( 1 ) ?   ( - 1   t o   e x i t )   " ) )  
 	 w h i l e ( c h o i c e   > =   0 ) :  
 	 	 #   i f   c h o i c e   = =   0 :  
 	 	 #   	 n   =   r a w _ i n p u t ( " N o t e   n a m e :   " )  
 	 	 #   	 n   =   t r a n s f o r m ( n )  
 	 	 #   	 t   =   i n t ( r a w _ i n p u t ( " N u m b e r   o f   h a l f - s t e p s   t o   t r a n s p o s e :   " ) )  
 	 	 #   	 p r i n t   t r a n s p o s e ( n ,   t )  
 	 	 i   =   M i d i I n s t r u m e n t ( )  
 	 	 i . m i d i _ i n s t r   =   6 9  
 	 	 f q   =   r a w _ i n p u t ( " F i l e ? ( y / n ) :   " )  
 	 	 i f   f q   = =   ' y ' :  
 	 	 	 f n a m e   =   r a w _ i n p u t ( " F i l e   n a m e :   " )  
 	 	 	 f n a m e   =   " i n p u t s / " + f n a m e  
 	 	 	 f i l e   =   o p e n ( f n a m e ,   " r " )  
 	 	 	 N o t e L   =   [ ]  
 	 	 	 k e y   =   f i l e . r e a d l i n e ( ) . s t r i p ( )  
 	 	 	 t r a n s f o r m ( k e y )  
 	 	 	 t i m e   =   i n t ( f i l e . r e a d l i n e ( ) . s t r i p ( ) )  
 	 	 	 n u m   =   i n t ( f i l e . r e a d l i n e ( ) . s t r i p ( ) )  
 	 	 	 f o r   i   i n   r a n g e ( n u m ) :  
 	 	 	 	 g e t =   f i l e . r e a d l i n e ( ) . s t r i p ( ) . s p l i t ( )  
 	 	 	 	 i f   ( l e n ( g e t )   = =   1 ) :  
 	 	 	 	 	 g e t . a p p e n d ( " 4 " )  
 	 	 	 	 g e t [ 0 ]   =   t r a n s f o r m ( g e t [ 0 ] )  
 	 	 	 	 n   =   g e t [ 0 ]   +   ' - '   +   g e t [ 1 ]  
 	 	 	 	 N o t e L . a p p e n d ( n )  
 	 	 	 t   =   w r i t e m u s i c ( N o t e L ,   t i m e ,   k e y ,   i )  
 	 	 	 c . a d d _ t r a c k ( t )  
 	 	 	 f i l e . c l o s e ( )  
 	 	 e l s e :  
 	 	 	 N o t e L   =   [ ]  
 	 	 	 k e y   =   r a w _ i n p u t ( " K e y   ( C a s e   s e n s i t i v e ) :   " )  
 	 	 	 t r a n s f o r m ( k e y )  
 	 	 	 t i m e   =   i n t ( i n p u t ( " B e a t s   p e r   m e a s u r e ( # / 4 ) :   " ) )  
 	 	 	 n u m   =   i n t ( i n p u t ( " N u m b e r   o f   n o t e s :   " ) )  
 	 	 	 f o r   i   i n   r a n g e ( n u m ) :  
 	 	 	 	 g e t =   r a w _ i n p u t ( " N o t e ( N A M E   O C T A V E   L E N G T H ) :   " ) . s p l i t ( )  
 	 	 	 	 i f   ( l e n ( g e t )   = =   1 ) :  
 	 	 	 	 	 g e t . a p p e n d ( " 4 " )  
 	 	 	 	 	 g e t . a p p e n d ( " q " )  
 	 	 	 	 e l i f   ( l e n ( g e t )   = =   2 ) :  
 	 	 	 	 	 g e t . a p p e n d ( " q " )  
 	 	 	 	 g e t [ 0 ]   =   t r a n s f o r m ( g e t [ 0 ] )  
 	 	 	 	 g e t [ 2 ]   =   g e t [ 2 ] . l o w e r ( )  
 	 	 	 	 n   =   g e t [ 0 ]   +   ' - '   +   g e t [ 1 ]  
 	 	 	 	 n F u l l   =   N o t e ( n ) . v a l u e  
 	 	 	 	 N o t e L . a p p e n d ( n )  
 	 	 	 t   =   w r i t e m u s i c ( N o t e L ,   t i m e ,   k e y ,   i )  
 	 	 	 c . a d d _ t r a c k ( t )  
  
 	 	 c . s e t _ a u t h o r ( " D a n i e l   A c k e r m a n s " ,   " a c k e r d 2 @ r p i . e d u " )  
 	 	 c . s e t _ t i t l e ( " C o m p o s i t i o n " )  
  
 	 	 t r   =   l o c a l t i m e ( N o n e )  
 	 	 t S   =   s t r u c t _ t i m e ( t r )  
 	 	 t i m e _ s t r i n g   =   " % s _ % s _ % s "   %   ( t S [ 0 ] ,   t S [ 1 ] ,   t S [ 2 ] )  
  
 	 	 o u t F i l e   =   r a w _ i n p u t ( " O u t f i l e   n a m e :   " )  
 	 	 p d f F   =   " p d f s / " + o u t F i l e + " . p d f "  
 	 	 m i d F   =   " m i d i F i l e s / " + o u t F i l e + " . m i d "  
 	 	 f i l e _ s t r i n g   =   " l o g s / h i s t o r y _ "   +   t i m e _ s t r i n g   +   " . t x t "  
  
 	 	 t e t   =   l i l y p o n d . f r o m _ C o m p o s i t i o n ( c )  
 	 	 l i l y p o n d . t o _ p d f ( t e t ,   p d f F )  
 	 	  
 	 	 h i s t   =   o p e n ( f i l e _ s t r i n g ,   " a " )  
 	 	 h i s t . w r i t e ( s t r ( a s c t i m e ( t r ) )   +   " \ n " )  
 	 	 h i s t . w r i t e ( t e t   +   " \ n " )  
 	 	 h i s t . w r i t e ( " \ n " )  
 	 	 h i s t . c l o s e ( )  
  
 	 	 #   m   =   m i d i _ f i l e _ o u t . M i d i F i l e ( [ t ] )  
 	 	 #   m . w r i t e _ f i l e ( m i d F )  
 	 	 m i d i _ f i l e _ o u t . w r i t e _ C o m p o s i t i o n ( m i d F ,   c ,   1 1 2 )  
  
  
 	 	 c h o i c e   =   i n t ( i n p u t ( " T r a n s p o s e ( 0 )   o r   W r i t e ( 1 ) ?   ( - 1   t o   e x i t )   " ) )