
yes:     file format elf64-x86-64


Disassembly of section .init:

0000000000002000 <.init>:
    2000:	f3 0f 1e fa          	endbr64 
    2004:	48 83 ec 08          	sub    $0x8,%rsp
    2008:	48 8b 05 31 6f 00 00 	mov    0x6f31(%rip),%rax        # 8f40 <__gmon_start__>
    200f:	48 85 c0             	test   %rax,%rax
    2012:	74 02                	je     2016 <__progname@@GLIBC_2.2.5-0x706a>
    2014:	ff d0                	callq  *%rax
    2016:	48 83 c4 08          	add    $0x8,%rsp
    201a:	c3                   	retq   

Disassembly of section .text:

0000000000002020 <.text>:
    2020:	ff 15 62 6e 00 00    	callq  *0x6e62(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    2026:	ff 15 5c 6e 00 00    	callq  *0x6e5c(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    202c:	ff 15 56 6e 00 00    	callq  *0x6e56(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    2032:	ff 15 50 6e 00 00    	callq  *0x6e50(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    2038:	ff 15 4a 6e 00 00    	callq  *0x6e4a(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    203e:	ff 15 44 6e 00 00    	callq  *0x6e44(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    2044:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    204b:	00 00 00 
    204e:	66 90                	xchg   %ax,%ax
    2050:	41 57                	push   %r15
    2052:	41 56                	push   %r14
    2054:	41 55                	push   %r13
    2056:	41 54                	push   %r12
    2058:	41 89 fc             	mov    %edi,%r12d
    205b:	55                   	push   %rbp
    205c:	53                   	push   %rbx
    205d:	48 89 f3             	mov    %rsi,%rbx
    2060:	48 83 ec 18          	sub    $0x18,%rsp
    2064:	48 8b 3e             	mov    (%rsi),%rdi
    2067:	67 e8 43 09 00 00    	addr32 callq 29b0 <__progname@@GLIBC_2.2.5-0x66d0>
    206d:	48 8d 35 cd 49 00 00 	lea    0x49cd(%rip),%rsi        # 6a41 <__progname@@GLIBC_2.2.5-0x263f>
    2074:	bf 06 00 00 00       	mov    $0x6,%edi
    2079:	ff 15 01 6f 00 00    	callq  *0x6f01(%rip)        # 8f80 <setlocale@GLIBC_2.2.5>
    207f:	48 8d 35 0a 40 00 00 	lea    0x400a(%rip),%rsi        # 6090 <__progname@@GLIBC_2.2.5-0x2ff0>
    2086:	48 8d 3d f5 3f 00 00 	lea    0x3ff5(%rip),%rdi        # 6082 <__progname@@GLIBC_2.2.5-0x2ffe>
    208d:	ff 15 3d 6e 00 00    	callq  *0x6e3d(%rip)        # 8ed0 <bindtextdomain@GLIBC_2.2.5>
    2093:	48 8d 3d e8 3f 00 00 	lea    0x3fe8(%rip),%rdi        # 6082 <__progname@@GLIBC_2.2.5-0x2ffe>
    209a:	ff 15 20 6e 00 00    	callq  *0x6e20(%rip)        # 8ec0 <textdomain@GLIBC_2.2.5>
    20a0:	48 8d 3d 99 06 00 00 	lea    0x699(%rip),%rdi        # 2740 <__progname@@GLIBC_2.2.5-0x6940>
    20a7:	67 e8 f3 33 00 00    	addr32 callq 54a0 <__progname@@GLIBC_2.2.5-0x3be0>
    20ad:	48 8d 05 ee 3f 00 00 	lea    0x3fee(%rip),%rax        # 60a2 <__progname@@GLIBC_2.2.5-0x2fde>
    20b4:	6a 00                	pushq  $0x0
    20b6:	4c 8d 0d 03 03 00 00 	lea    0x303(%rip),%r9        # 23c0 <__progname@@GLIBC_2.2.5-0x6cc0>
    20bd:	50                   	push   %rax
    20be:	4c 8b 05 4b 6f 00 00 	mov    0x6f4b(%rip),%r8        # 9010 <__progname@@GLIBC_2.2.5-0x70>
    20c5:	48 89 de             	mov    %rbx,%rsi
    20c8:	44 89 e7             	mov    %r12d,%edi
    20cb:	48 8d 0d ac 3f 00 00 	lea    0x3fac(%rip),%rcx        # 607e <__progname@@GLIBC_2.2.5-0x3002>
    20d2:	48 8d 15 2b 3f 00 00 	lea    0x3f2b(%rip),%rdx        # 6004 <__progname@@GLIBC_2.2.5-0x307c>
    20d9:	31 c0                	xor    %eax,%eax
    20db:	67 e8 8f 07 00 00    	addr32 callq 2870 <__progname@@GLIBC_2.2.5-0x6810>
    20e1:	45 31 c0             	xor    %r8d,%r8d
    20e4:	48 89 de             	mov    %rbx,%rsi
    20e7:	44 89 e7             	mov    %r12d,%edi
    20ea:	48 8d 0d af 41 00 00 	lea    0x41af(%rip),%rcx        # 62a0 <__progname@@GLIBC_2.2.5-0x2de0>
    20f1:	48 8d 15 ba 3f 00 00 	lea    0x3fba(%rip),%rdx        # 60b2 <__progname@@GLIBC_2.2.5-0x2fce>
    20f8:	ff 15 fa 6d 00 00    	callq  *0x6dfa(%rip)        # 8ef8 <getopt_long@GLIBC_2.2.5>
    20fe:	5a                   	pop    %rdx
    20ff:	59                   	pop    %rcx
    2100:	83 f8 ff             	cmp    $0xffffffff,%eax
    2103:	0f 85 9c 01 00 00    	jne    22a5 <__progname@@GLIBC_2.2.5-0x6ddb>
    2109:	48 63 15 80 6f 00 00 	movslq 0x6f80(%rip),%rdx        # 9090 <optind@@GLIBC_2.2.5>
    2110:	48 89 d0             	mov    %rdx,%rax
    2113:	48 8d 2c d3          	lea    (%rbx,%rdx,8),%rbp
    2117:	49 63 d4             	movslq %r12d,%rdx
    211a:	4c 8d 34 d3          	lea    (%rbx,%rdx,8),%r14
    211e:	44 39 e0             	cmp    %r12d,%eax
    2121:	75 0f                	jne    2132 <__progname@@GLIBC_2.2.5-0x6f4e>
    2123:	48 8d 05 8a 3f 00 00 	lea    0x3f8a(%rip),%rax        # 60b4 <__progname@@GLIBC_2.2.5-0x2fcc>
    212a:	49 83 c6 08          	add    $0x8,%r14
    212e:	49 89 46 f8          	mov    %rax,-0x8(%r14)
    2132:	49 39 ee             	cmp    %rbp,%r14
    2135:	0f 86 74 01 00 00    	jbe    22af <__progname@@GLIBC_2.2.5-0x6dd1>
    213b:	4c 8b 6d 00          	mov    0x0(%rbp),%r13
    213f:	48 89 eb             	mov    %rbp,%rbx
    2142:	41 bf 01 00 00 00    	mov    $0x1,%r15d
    2148:	45 31 e4             	xor    %r12d,%r12d
    214b:	4c 89 e9             	mov    %r13,%rcx
    214e:	66 90                	xchg   %ax,%ax
    2150:	48 89 cf             	mov    %rcx,%rdi
    2153:	48 89 4c 24 08       	mov    %rcx,0x8(%rsp)
    2158:	48 83 c3 08          	add    $0x8,%rbx
    215c:	ff 15 86 6d 00 00    	callq  *0x6d86(%rip)        # 8ee8 <strlen@GLIBC_2.2.5>
    2162:	48 83 c0 01          	add    $0x1,%rax
    2166:	49 01 c4             	add    %rax,%r12
    2169:	4c 39 f3             	cmp    %r14,%rbx
    216c:	0f 82 7e 00 00 00    	jb     21f0 <__progname@@GLIBC_2.2.5-0x6e90>
    2172:	49 81 fc 00 10 00 00 	cmp    $0x1000,%r12
    2179:	76 5d                	jbe    21d8 <__progname@@GLIBC_2.2.5-0x6ea8>
    217b:	45 84 ff             	test   %r15b,%r15b
    217e:	74 5e                	je     21de <__progname@@GLIBC_2.2.5-0x6ea2>
    2180:	31 db                	xor    %ebx,%ebx
    2182:	eb 1b                	jmp    219f <__progname@@GLIBC_2.2.5-0x6ee1>
    2184:	0f 1f 40 00          	nopl   0x0(%rax)
    2188:	48 8d 04 19          	lea    (%rcx,%rbx,1),%rax
    218c:	48 83 c5 08          	add    $0x8,%rbp
    2190:	48 8d 58 01          	lea    0x1(%rax),%rbx
    2194:	4c 01 e8             	add    %r13,%rax
    2197:	c6 00 20             	movb   $0x20,(%rax)
    219a:	49 39 ee             	cmp    %rbp,%r14
    219d:	76 71                	jbe    2210 <__progname@@GLIBC_2.2.5-0x6e70>
    219f:	48 8b 75 00          	mov    0x0(%rbp),%rsi
    21a3:	48 89 f7             	mov    %rsi,%rdi
    21a6:	48 89 74 24 08       	mov    %rsi,0x8(%rsp)
    21ab:	ff 15 37 6d 00 00    	callq  *0x6d37(%rip)        # 8ee8 <strlen@GLIBC_2.2.5>
    21b1:	45 84 ff             	test   %r15b,%r15b
    21b4:	48 8b 74 24 08       	mov    0x8(%rsp),%rsi
    21b9:	48 89 c1             	mov    %rax,%rcx
    21bc:	75 ca                	jne    2188 <__progname@@GLIBC_2.2.5-0x6ef8>
    21be:	49 8d 7c 1d 00       	lea    0x0(%r13,%rbx,1),%rdi
    21c3:	48 89 c2             	mov    %rax,%rdx
    21c6:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    21cb:	ff 15 77 6d 00 00    	callq  *0x6d77(%rip)        # 8f48 <memcpy@GLIBC_2.14>
    21d1:	48 8b 4c 24 08       	mov    0x8(%rsp),%rcx
    21d6:	eb b0                	jmp    2188 <__progname@@GLIBC_2.2.5-0x6ef8>
    21d8:	41 bc 00 20 00 00    	mov    $0x2000,%r12d
    21de:	4c 89 e7             	mov    %r12,%rdi
    21e1:	45 31 ff             	xor    %r15d,%r15d
    21e4:	67 e8 b6 2c 00 00    	addr32 callq 4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    21ea:	49 89 c5             	mov    %rax,%r13
    21ed:	eb 91                	jmp    2180 <__progname@@GLIBC_2.2.5-0x6f00>
    21ef:	90                   	nop
    21f0:	48 8b 4c 24 08       	mov    0x8(%rsp),%rcx
    21f5:	48 01 c8             	add    %rcx,%rax
    21f8:	48 8b 0b             	mov    (%rbx),%rcx
    21fb:	48 39 c8             	cmp    %rcx,%rax
    21fe:	b8 00 00 00 00       	mov    $0x0,%eax
    2203:	44 0f 45 f8          	cmovne %eax,%r15d
    2207:	e9 44 ff ff ff       	jmpq   2150 <__progname@@GLIBC_2.2.5-0x6f30>
    220c:	0f 1f 40 00          	nopl   0x0(%rax)
    2210:	c6 00 0a             	movb   $0xa,(%rax)
    2213:	31 d2                	xor    %edx,%edx
    2215:	4c 89 e0             	mov    %r12,%rax
    2218:	48 f7 f3             	div    %rbx
    221b:	48 89 c5             	mov    %rax,%rbp
    221e:	49 89 c4             	mov    %rax,%r12
    2221:	48 83 ed 01          	sub    $0x1,%rbp
    2225:	74 28                	je     224f <__progname@@GLIBC_2.2.5-0x6e31>
    2227:	49 8d 4c 1d 00       	lea    0x0(%r13,%rbx,1),%rcx
    222c:	0f 1f 40 00          	nopl   0x0(%rax)
    2230:	48 89 cf             	mov    %rcx,%rdi
    2233:	48 89 da             	mov    %rbx,%rdx
    2236:	4c 89 ee             	mov    %r13,%rsi
    2239:	ff 15 09 6d 00 00    	callq  *0x6d09(%rip)        # 8f48 <memcpy@GLIBC_2.14>
    223f:	48 89 c1             	mov    %rax,%rcx
    2242:	48 01 d9             	add    %rbx,%rcx
    2245:	48 83 ed 01          	sub    $0x1,%rbp
    2249:	75 e5                	jne    2230 <__progname@@GLIBC_2.2.5-0x6e50>
    224b:	49 0f af dc          	imul   %r12,%rbx
    224f:	48 89 da             	mov    %rbx,%rdx
    2252:	4c 89 ee             	mov    %r13,%rsi
    2255:	bf 01 00 00 00       	mov    $0x1,%edi
    225a:	67 e8 90 05 00 00    	addr32 callq 27f0 <__progname@@GLIBC_2.2.5-0x6890>
    2260:	48 39 d8             	cmp    %rbx,%rax
    2263:	74 ea                	je     224f <__progname@@GLIBC_2.2.5-0x6e31>
    2265:	ba 05 00 00 00       	mov    $0x5,%edx
    226a:	48 8d 35 45 3e 00 00 	lea    0x3e45(%rip),%rsi        # 60b6 <__progname@@GLIBC_2.2.5-0x2fca>
    2271:	31 ff                	xor    %edi,%edi
    2273:	ff 15 5f 6c 00 00    	callq  *0x6c5f(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    2279:	48 89 c3             	mov    %rax,%rbx
    227c:	ff 15 0e 6c 00 00    	callq  *0x6c0e(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    2282:	48 89 da             	mov    %rbx,%rdx
    2285:	31 ff                	xor    %edi,%edi
    2287:	8b 30                	mov    (%rax),%esi
    2289:	31 c0                	xor    %eax,%eax
    228b:	ff 15 ff 6c 00 00    	callq  *0x6cff(%rip)        # 8f90 <error@GLIBC_2.2.5>
    2291:	48 83 c4 18          	add    $0x18,%rsp
    2295:	b8 01 00 00 00       	mov    $0x1,%eax
    229a:	5b                   	pop    %rbx
    229b:	5d                   	pop    %rbp
    229c:	41 5c                	pop    %r12
    229e:	41 5d                	pop    %r13
    22a0:	41 5e                	pop    %r14
    22a2:	41 5f                	pop    %r15
    22a4:	c3                   	retq   
    22a5:	bf 01 00 00 00       	mov    $0x1,%edi
    22aa:	e8 11 01 00 00       	callq  23c0 <__progname@@GLIBC_2.2.5-0x6cc0>
    22af:	bf 00 20 00 00       	mov    $0x2000,%edi
    22b4:	67 e8 e6 2b 00 00    	addr32 callq 4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    22ba:	c6 40 ff 0a          	movb   $0xa,-0x1(%rax)
    22be:	0f 0b                	ud2    
    22c0:	f3 0f 1e fa          	endbr64 
    22c4:	31 ed                	xor    %ebp,%ebp
    22c6:	49 89 d1             	mov    %rdx,%r9
    22c9:	5e                   	pop    %rsi
    22ca:	48 89 e2             	mov    %rsp,%rdx
    22cd:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    22d1:	50                   	push   %rax
    22d2:	54                   	push   %rsp
    22d3:	4c 8d 05 b6 31 00 00 	lea    0x31b6(%rip),%r8        # 5490 <__progname@@GLIBC_2.2.5-0x3bf0>
    22da:	48 8d 0d 3f 31 00 00 	lea    0x313f(%rip),%rcx        # 5420 <__progname@@GLIBC_2.2.5-0x3c60>
    22e1:	48 8d 3d 68 fd ff ff 	lea    -0x298(%rip),%rdi        # 2050 <__progname@@GLIBC_2.2.5-0x7030>
    22e8:	ff 15 32 6c 00 00    	callq  *0x6c32(%rip)        # 8f20 <__libc_start_main@GLIBC_2.2.5>
    22ee:	f4                   	hlt    
    22ef:	90                   	nop
    22f0:	48 8d 3d 89 6d 00 00 	lea    0x6d89(%rip),%rdi        # 9080 <__progname@@GLIBC_2.2.5>
    22f7:	48 8d 05 82 6d 00 00 	lea    0x6d82(%rip),%rax        # 9080 <__progname@@GLIBC_2.2.5>
    22fe:	48 39 f8             	cmp    %rdi,%rax
    2301:	74 15                	je     2318 <__progname@@GLIBC_2.2.5-0x6d68>
    2303:	48 8b 05 96 6b 00 00 	mov    0x6b96(%rip),%rax        # 8ea0 <_ITM_deregisterTMCloneTable>
    230a:	48 85 c0             	test   %rax,%rax
    230d:	74 09                	je     2318 <__progname@@GLIBC_2.2.5-0x6d68>
    230f:	ff e0                	jmpq   *%rax
    2311:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    2318:	c3                   	retq   
    2319:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    2320:	48 8d 3d 59 6d 00 00 	lea    0x6d59(%rip),%rdi        # 9080 <__progname@@GLIBC_2.2.5>
    2327:	48 8d 35 52 6d 00 00 	lea    0x6d52(%rip),%rsi        # 9080 <__progname@@GLIBC_2.2.5>
    232e:	48 29 fe             	sub    %rdi,%rsi
    2331:	48 c1 fe 03          	sar    $0x3,%rsi
    2335:	48 89 f0             	mov    %rsi,%rax
    2338:	48 c1 e8 3f          	shr    $0x3f,%rax
    233c:	48 01 c6             	add    %rax,%rsi
    233f:	48 d1 fe             	sar    %rsi
    2342:	74 14                	je     2358 <__progname@@GLIBC_2.2.5-0x6d28>
    2344:	48 8b 05 75 6c 00 00 	mov    0x6c75(%rip),%rax        # 8fc0 <_ITM_registerTMCloneTable>
    234b:	48 85 c0             	test   %rax,%rax
    234e:	74 08                	je     2358 <__progname@@GLIBC_2.2.5-0x6d28>
    2350:	ff e0                	jmpq   *%rax
    2352:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    2358:	c3                   	retq   
    2359:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    2360:	f3 0f 1e fa          	endbr64 
    2364:	80 3d 5d 6d 00 00 00 	cmpb   $0x0,0x6d5d(%rip)        # 90c8 <stderr@@GLIBC_2.2.5+0x8>
    236b:	75 33                	jne    23a0 <__progname@@GLIBC_2.2.5-0x6ce0>
    236d:	55                   	push   %rbp
    236e:	48 83 3d 62 6c 00 00 	cmpq   $0x0,0x6c62(%rip)        # 8fd8 <__cxa_finalize@GLIBC_2.2.5>
    2375:	00 
    2376:	48 89 e5             	mov    %rsp,%rbp
    2379:	74 0d                	je     2388 <__progname@@GLIBC_2.2.5-0x6cf8>
    237b:	48 8b 3d 86 6c 00 00 	mov    0x6c86(%rip),%rdi        # 9008 <__progname@@GLIBC_2.2.5-0x78>
    2382:	ff 15 50 6c 00 00    	callq  *0x6c50(%rip)        # 8fd8 <__cxa_finalize@GLIBC_2.2.5>
    2388:	e8 63 ff ff ff       	callq  22f0 <__progname@@GLIBC_2.2.5-0x6d90>
    238d:	c6 05 34 6d 00 00 01 	movb   $0x1,0x6d34(%rip)        # 90c8 <stderr@@GLIBC_2.2.5+0x8>
    2394:	5d                   	pop    %rbp
    2395:	c3                   	retq   
    2396:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    239d:	00 00 00 
    23a0:	c3                   	retq   
    23a1:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    23a8:	00 00 00 00 
    23ac:	0f 1f 40 00          	nopl   0x0(%rax)
    23b0:	f3 0f 1e fa          	endbr64 
    23b4:	e9 67 ff ff ff       	jmpq   2320 <__progname@@GLIBC_2.2.5-0x6d60>
    23b9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    23c0:	41 54                	push   %r12
    23c2:	ba 05 00 00 00       	mov    $0x5,%edx
    23c7:	55                   	push   %rbp
    23c8:	53                   	push   %rbx
    23c9:	89 fb                	mov    %edi,%ebx
    23cb:	48 83 c4 80          	add    $0xffffffffffffff80,%rsp
    23cf:	48 8b 2d 0a 6d 00 00 	mov    0x6d0a(%rip),%rbp        # 90e0 <stderr@@GLIBC_2.2.5+0x20>
    23d6:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    23dd:	00 00 
    23df:	48 89 44 24 78       	mov    %rax,0x78(%rsp)
    23e4:	31 c0                	xor    %eax,%eax
    23e6:	85 ff                	test   %edi,%edi
    23e8:	74 31                	je     241b <__progname@@GLIBC_2.2.5-0x6c65>
    23ea:	48 8d 35 d7 3c 00 00 	lea    0x3cd7(%rip),%rsi        # 60c8 <__progname@@GLIBC_2.2.5-0x2fb8>
    23f1:	31 ff                	xor    %edi,%edi
    23f3:	ff 15 df 6a 00 00    	callq  *0x6adf(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    23f9:	48 89 e9             	mov    %rbp,%rcx
    23fc:	be 01 00 00 00       	mov    $0x1,%esi
    2401:	48 8b 3d b8 6c 00 00 	mov    0x6cb8(%rip),%rdi        # 90c0 <stderr@@GLIBC_2.2.5>
    2408:	48 89 c2             	mov    %rax,%rdx
    240b:	31 c0                	xor    %eax,%eax
    240d:	ff 15 a5 6b 00 00    	callq  *0x6ba5(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    2413:	89 df                	mov    %ebx,%edi
    2415:	ff 15 8d 6b 00 00    	callq  *0x6b8d(%rip)        # 8fa8 <exit@GLIBC_2.2.5>
    241b:	48 8d 35 ce 3c 00 00 	lea    0x3cce(%rip),%rsi        # 60f0 <__progname@@GLIBC_2.2.5-0x2f90>
    2422:	31 ff                	xor    %edi,%edi
    2424:	ff 15 ae 6a 00 00    	callq  *0x6aae(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    242a:	48 89 e9             	mov    %rbp,%rcx
    242d:	48 89 ea             	mov    %rbp,%rdx
    2430:	bf 01 00 00 00       	mov    $0x1,%edi
    2435:	48 89 c6             	mov    %rax,%rsi
    2438:	31 c0                	xor    %eax,%eax
    243a:	ff 15 48 6b 00 00    	callq  *0x6b48(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    2440:	48 8b 2d 41 6c 00 00 	mov    0x6c41(%rip),%rbp        # 9088 <stdout@@GLIBC_2.2.5>
    2447:	ba 05 00 00 00       	mov    $0x5,%edx
    244c:	31 ff                	xor    %edi,%edi
    244e:	48 8d 35 c3 3c 00 00 	lea    0x3cc3(%rip),%rsi        # 6118 <__progname@@GLIBC_2.2.5-0x2f68>
    2455:	ff 15 7d 6a 00 00    	callq  *0x6a7d(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    245b:	48 89 ee             	mov    %rbp,%rsi
    245e:	48 89 c7             	mov    %rax,%rdi
    2461:	ff 15 c9 6a 00 00    	callq  *0x6ac9(%rip)        # 8f30 <fputs_unlocked@GLIBC_2.2.5>
    2467:	48 8b 2d 1a 6c 00 00 	mov    0x6c1a(%rip),%rbp        # 9088 <stdout@@GLIBC_2.2.5>
    246e:	ba 05 00 00 00       	mov    $0x5,%edx
    2473:	31 ff                	xor    %edi,%edi
    2475:	48 8d 35 e4 3c 00 00 	lea    0x3ce4(%rip),%rsi        # 6160 <__progname@@GLIBC_2.2.5-0x2f20>
    247c:	ff 15 56 6a 00 00    	callq  *0x6a56(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    2482:	48 89 ee             	mov    %rbp,%rsi
    2485:	48 89 c7             	mov    %rax,%rdi
    2488:	ff 15 a2 6a 00 00    	callq  *0x6aa2(%rip)        # 8f30 <fputs_unlocked@GLIBC_2.2.5>
    248e:	48 8b 2d f3 6b 00 00 	mov    0x6bf3(%rip),%rbp        # 9088 <stdout@@GLIBC_2.2.5>
    2495:	ba 05 00 00 00       	mov    $0x5,%edx
    249a:	31 ff                	xor    %edi,%edi
    249c:	48 8d 35 ed 3c 00 00 	lea    0x3ced(%rip),%rsi        # 6190 <__progname@@GLIBC_2.2.5-0x2ef0>
    24a3:	ff 15 2f 6a 00 00    	callq  *0x6a2f(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    24a9:	48 89 ee             	mov    %rbp,%rsi
    24ac:	48 8d 2d 51 3b 00 00 	lea    0x3b51(%rip),%rbp        # 6004 <__progname@@GLIBC_2.2.5-0x307c>
    24b3:	48 89 c7             	mov    %rax,%rdi
    24b6:	ff 15 74 6a 00 00    	callq  *0x6a74(%rip)        # 8f30 <fputs_unlocked@GLIBC_2.2.5>
    24bc:	48 8d 05 45 3b 00 00 	lea    0x3b45(%rip),%rax        # 6008 <__progname@@GLIBC_2.2.5-0x3078>
    24c3:	48 8d 0d 7f 3b 00 00 	lea    0x3b7f(%rip),%rcx        # 6049 <__progname@@GLIBC_2.2.5-0x3037>
    24ca:	48 c7 44 24 60 00 00 	movq   $0x0,0x60(%rsp)
    24d1:	00 00 
    24d3:	48 89 04 24          	mov    %rax,(%rsp)
    24d7:	48 8d 05 2c 3b 00 00 	lea    0x3b2c(%rip),%rax        # 600a <__progname@@GLIBC_2.2.5-0x3076>
    24de:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    24e3:	48 8d 05 98 3b 00 00 	lea    0x3b98(%rip),%rax        # 6082 <__progname@@GLIBC_2.2.5-0x2ffe>
    24ea:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
    24ef:	48 8d 0d 5d 3b 00 00 	lea    0x3b5d(%rip),%rcx        # 6053 <__progname@@GLIBC_2.2.5-0x302d>
    24f6:	48 89 44 24 10       	mov    %rax,0x10(%rsp)
    24fb:	48 8d 05 18 3b 00 00 	lea    0x3b18(%rip),%rax        # 601a <__progname@@GLIBC_2.2.5-0x3066>
    2502:	48 89 4c 24 40       	mov    %rcx,0x40(%rsp)
    2507:	48 8d 0d 4f 3b 00 00 	lea    0x3b4f(%rip),%rcx        # 605d <__progname@@GLIBC_2.2.5-0x3023>
    250e:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    2513:	48 8d 05 16 3b 00 00 	lea    0x3b16(%rip),%rax        # 6030 <__progname@@GLIBC_2.2.5-0x3050>
    251a:	48 89 4c 24 50       	mov    %rcx,0x50(%rsp)
    251f:	48 c7 44 24 68 00 00 	movq   $0x0,0x68(%rsp)
    2526:	00 00 
    2528:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
    252d:	48 8d 05 06 3b 00 00 	lea    0x3b06(%rip),%rax        # 603a <__progname@@GLIBC_2.2.5-0x3046>
    2534:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
    2539:	48 89 44 24 38       	mov    %rax,0x38(%rsp)
    253e:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    2543:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
    2548:	48 89 e0             	mov    %rsp,%rax
    254b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    2550:	48 83 c0 10          	add    $0x10,%rax
    2554:	48 8b 38             	mov    (%rax),%rdi
    2557:	48 85 ff             	test   %rdi,%rdi
    255a:	74 14                	je     2570 <__progname@@GLIBC_2.2.5-0x6b10>
    255c:	b9 04 00 00 00       	mov    $0x4,%ecx
    2561:	48 89 ee             	mov    %rbp,%rsi
    2564:	f3 a6                	repz cmpsb %es:(%rdi),%ds:(%rsi)
    2566:	0f 97 c2             	seta   %dl
    2569:	80 da 00             	sbb    $0x0,%dl
    256c:	84 d2                	test   %dl,%dl
    256e:	75 e0                	jne    2550 <__progname@@GLIBC_2.2.5-0x6b30>
    2570:	4c 8b 60 08          	mov    0x8(%rax),%r12
    2574:	ba 05 00 00 00       	mov    $0x5,%edx
    2579:	48 8d 35 e7 3a 00 00 	lea    0x3ae7(%rip),%rsi        # 6067 <__progname@@GLIBC_2.2.5-0x3019>
    2580:	31 ff                	xor    %edi,%edi
    2582:	4d 85 e4             	test   %r12,%r12
    2585:	0f 84 c9 00 00 00    	je     2654 <__progname@@GLIBC_2.2.5-0x6a2c>
    258b:	ff 15 47 69 00 00    	callq  *0x6947(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    2591:	bf 01 00 00 00       	mov    $0x1,%edi
    2596:	48 8d 0d 2b 3c 00 00 	lea    0x3c2b(%rip),%rcx        # 61c8 <__progname@@GLIBC_2.2.5-0x2eb8>
    259d:	48 8d 15 da 3a 00 00 	lea    0x3ada(%rip),%rdx        # 607e <__progname@@GLIBC_2.2.5-0x3002>
    25a4:	48 89 c6             	mov    %rax,%rsi
    25a7:	31 c0                	xor    %eax,%eax
    25a9:	ff 15 d9 69 00 00    	callq  *0x69d9(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    25af:	31 f6                	xor    %esi,%esi
    25b1:	bf 05 00 00 00       	mov    $0x5,%edi
    25b6:	ff 15 c4 69 00 00    	callq  *0x69c4(%rip)        # 8f80 <setlocale@GLIBC_2.2.5>
    25bc:	48 85 c0             	test   %rax,%rax
    25bf:	74 1d                	je     25de <__progname@@GLIBC_2.2.5-0x6aa2>
    25c1:	ba 03 00 00 00       	mov    $0x3,%edx
    25c6:	48 8d 35 bf 3a 00 00 	lea    0x3abf(%rip),%rsi        # 608c <__progname@@GLIBC_2.2.5-0x2ff4>
    25cd:	48 89 c7             	mov    %rax,%rdi
    25d0:	ff 15 c2 68 00 00    	callq  *0x68c2(%rip)        # 8e98 <strncmp@GLIBC_2.2.5>
    25d6:	85 c0                	test   %eax,%eax
    25d8:	0f 85 11 01 00 00    	jne    26ef <__progname@@GLIBC_2.2.5-0x6991>
    25de:	31 ff                	xor    %edi,%edi
    25e0:	ba 05 00 00 00       	mov    $0x5,%edx
    25e5:	48 8d 35 4c 3c 00 00 	lea    0x3c4c(%rip),%rsi        # 6238 <__progname@@GLIBC_2.2.5-0x2e48>
    25ec:	ff 15 e6 68 00 00    	callq  *0x68e6(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    25f2:	48 8d 0d 0b 3a 00 00 	lea    0x3a0b(%rip),%rcx        # 6004 <__progname@@GLIBC_2.2.5-0x307c>
    25f9:	bf 01 00 00 00       	mov    $0x1,%edi
    25fe:	48 8d 15 c3 3b 00 00 	lea    0x3bc3(%rip),%rdx        # 61c8 <__progname@@GLIBC_2.2.5-0x2eb8>
    2605:	48 89 c6             	mov    %rax,%rsi
    2608:	31 c0                	xor    %eax,%eax
    260a:	ff 15 78 69 00 00    	callq  *0x6978(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    2610:	49 39 ec             	cmp    %rbp,%r12
    2613:	48 8d 0d 27 44 00 00 	lea    0x4427(%rip),%rcx        # 6a41 <__progname@@GLIBC_2.2.5-0x263f>
    261a:	48 8d 2d 03 3a 00 00 	lea    0x3a03(%rip),%rbp        # 6024 <__progname@@GLIBC_2.2.5-0x305c>
    2621:	48 0f 45 e9          	cmovne %rcx,%rbp
    2625:	31 ff                	xor    %edi,%edi
    2627:	48 8d 35 2a 3c 00 00 	lea    0x3c2a(%rip),%rsi        # 6258 <__progname@@GLIBC_2.2.5-0x2e28>
    262e:	ba 05 00 00 00       	mov    $0x5,%edx
    2633:	ff 15 9f 68 00 00    	callq  *0x689f(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    2639:	48 89 e9             	mov    %rbp,%rcx
    263c:	4c 89 e2             	mov    %r12,%rdx
    263f:	bf 01 00 00 00       	mov    $0x1,%edi
    2644:	48 89 c6             	mov    %rax,%rsi
    2647:	31 c0                	xor    %eax,%eax
    2649:	ff 15 39 69 00 00    	callq  *0x6939(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    264f:	e9 bf fd ff ff       	jmpq   2413 <__progname@@GLIBC_2.2.5-0x6c6d>
    2654:	ff 15 7e 68 00 00    	callq  *0x687e(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    265a:	bf 01 00 00 00       	mov    $0x1,%edi
    265f:	48 8d 0d 62 3b 00 00 	lea    0x3b62(%rip),%rcx        # 61c8 <__progname@@GLIBC_2.2.5-0x2eb8>
    2666:	48 8d 15 11 3a 00 00 	lea    0x3a11(%rip),%rdx        # 607e <__progname@@GLIBC_2.2.5-0x3002>
    266d:	48 89 c6             	mov    %rax,%rsi
    2670:	31 c0                	xor    %eax,%eax
    2672:	ff 15 10 69 00 00    	callq  *0x6910(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    2678:	31 f6                	xor    %esi,%esi
    267a:	bf 05 00 00 00       	mov    $0x5,%edi
    267f:	ff 15 fb 68 00 00    	callq  *0x68fb(%rip)        # 8f80 <setlocale@GLIBC_2.2.5>
    2685:	48 85 c0             	test   %rax,%rax
    2688:	74 19                	je     26a3 <__progname@@GLIBC_2.2.5-0x69dd>
    268a:	ba 03 00 00 00       	mov    $0x3,%edx
    268f:	48 8d 35 f6 39 00 00 	lea    0x39f6(%rip),%rsi        # 608c <__progname@@GLIBC_2.2.5-0x2ff4>
    2696:	48 89 c7             	mov    %rax,%rdi
    2699:	ff 15 f9 67 00 00    	callq  *0x67f9(%rip)        # 8e98 <strncmp@GLIBC_2.2.5>
    269f:	85 c0                	test   %eax,%eax
    26a1:	75 45                	jne    26e8 <__progname@@GLIBC_2.2.5-0x6998>
    26a3:	ba 05 00 00 00       	mov    $0x5,%edx
    26a8:	48 8d 35 89 3b 00 00 	lea    0x3b89(%rip),%rsi        # 6238 <__progname@@GLIBC_2.2.5-0x2e48>
    26af:	31 ff                	xor    %edi,%edi
    26b1:	ff 15 21 68 00 00    	callq  *0x6821(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    26b7:	4c 8d 25 46 39 00 00 	lea    0x3946(%rip),%r12        # 6004 <__progname@@GLIBC_2.2.5-0x307c>
    26be:	48 8d 0d 3f 39 00 00 	lea    0x393f(%rip),%rcx        # 6004 <__progname@@GLIBC_2.2.5-0x307c>
    26c5:	bf 01 00 00 00       	mov    $0x1,%edi
    26ca:	48 89 c6             	mov    %rax,%rsi
    26cd:	48 8d 15 f4 3a 00 00 	lea    0x3af4(%rip),%rdx        # 61c8 <__progname@@GLIBC_2.2.5-0x2eb8>
    26d4:	31 c0                	xor    %eax,%eax
    26d6:	ff 15 ac 68 00 00    	callq  *0x68ac(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    26dc:	48 8d 2d 41 39 00 00 	lea    0x3941(%rip),%rbp        # 6024 <__progname@@GLIBC_2.2.5-0x305c>
    26e3:	e9 3d ff ff ff       	jmpq   2625 <__progname@@GLIBC_2.2.5-0x6a5b>
    26e8:	4c 8d 25 15 39 00 00 	lea    0x3915(%rip),%r12        # 6004 <__progname@@GLIBC_2.2.5-0x307c>
    26ef:	31 ff                	xor    %edi,%edi
    26f1:	ba 05 00 00 00       	mov    $0x5,%edx
    26f6:	48 8d 35 f3 3a 00 00 	lea    0x3af3(%rip),%rsi        # 61f0 <__progname@@GLIBC_2.2.5-0x2e90>
    26fd:	ff 15 d5 67 00 00    	callq  *0x67d5(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    2703:	48 8d 15 fa 38 00 00 	lea    0x38fa(%rip),%rdx        # 6004 <__progname@@GLIBC_2.2.5-0x307c>
    270a:	bf 01 00 00 00       	mov    $0x1,%edi
    270f:	48 89 c6             	mov    %rax,%rsi
    2712:	31 c0                	xor    %eax,%eax
    2714:	ff 15 6e 68 00 00    	callq  *0x686e(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    271a:	e9 bf fe ff ff       	jmpq   25de <__progname@@GLIBC_2.2.5-0x6aa2>
    271f:	90                   	nop
    2720:	48 89 3d b1 69 00 00 	mov    %rdi,0x69b1(%rip)        # 90d8 <stderr@@GLIBC_2.2.5+0x18>
    2727:	c3                   	retq   
    2728:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    272f:	00 
    2730:	40 88 3d 99 69 00 00 	mov    %dil,0x6999(%rip)        # 90d0 <stderr@@GLIBC_2.2.5+0x10>
    2737:	c3                   	retq   
    2738:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    273f:	00 
    2740:	55                   	push   %rbp
    2741:	53                   	push   %rbx
    2742:	48 83 ec 08          	sub    $0x8,%rsp
    2746:	48 8b 3d 3b 69 00 00 	mov    0x693b(%rip),%rdi        # 9088 <stdout@@GLIBC_2.2.5>
    274d:	67 e8 7d 2a 00 00    	addr32 callq 51d0 <__progname@@GLIBC_2.2.5-0x3eb0>
    2753:	85 c0                	test   %eax,%eax
    2755:	74 17                	je     276e <__progname@@GLIBC_2.2.5-0x6912>
    2757:	ff 15 33 67 00 00    	callq  *0x6733(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    275d:	80 3d 6c 69 00 00 00 	cmpb   $0x0,0x696c(%rip)        # 90d0 <stderr@@GLIBC_2.2.5+0x10>
    2764:	48 89 c3             	mov    %rax,%rbx
    2767:	74 1d                	je     2786 <__progname@@GLIBC_2.2.5-0x68fa>
    2769:	83 38 20             	cmpl   $0x20,(%rax)
    276c:	75 18                	jne    2786 <__progname@@GLIBC_2.2.5-0x68fa>
    276e:	48 8b 3d 4b 69 00 00 	mov    0x694b(%rip),%rdi        # 90c0 <stderr@@GLIBC_2.2.5>
    2775:	67 e8 55 2a 00 00    	addr32 callq 51d0 <__progname@@GLIBC_2.2.5-0x3eb0>
    277b:	85 c0                	test   %eax,%eax
    277d:	75 49                	jne    27c8 <__progname@@GLIBC_2.2.5-0x68b8>
    277f:	48 83 c4 08          	add    $0x8,%rsp
    2783:	5b                   	pop    %rbx
    2784:	5d                   	pop    %rbp
    2785:	c3                   	retq   
    2786:	31 ff                	xor    %edi,%edi
    2788:	ba 05 00 00 00       	mov    $0x5,%edx
    278d:	48 8d 35 31 3b 00 00 	lea    0x3b31(%rip),%rsi        # 62c5 <__progname@@GLIBC_2.2.5-0x2dbb>
    2794:	ff 15 3e 67 00 00    	callq  *0x673e(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    279a:	48 8b 3d 37 69 00 00 	mov    0x6937(%rip),%rdi        # 90d8 <stderr@@GLIBC_2.2.5+0x18>
    27a1:	48 89 c5             	mov    %rax,%rbp
    27a4:	48 85 ff             	test   %rdi,%rdi
    27a7:	74 2b                	je     27d4 <__progname@@GLIBC_2.2.5-0x68ac>
    27a9:	67 e8 01 1e 00 00    	addr32 callq 45b0 <__progname@@GLIBC_2.2.5-0x4ad0>
    27af:	49 89 e8             	mov    %rbp,%r8
    27b2:	8b 33                	mov    (%rbx),%esi
    27b4:	31 ff                	xor    %edi,%edi
    27b6:	48 89 c1             	mov    %rax,%rcx
    27b9:	48 8d 15 11 3b 00 00 	lea    0x3b11(%rip),%rdx        # 62d1 <__progname@@GLIBC_2.2.5-0x2daf>
    27c0:	31 c0                	xor    %eax,%eax
    27c2:	ff 15 c8 67 00 00    	callq  *0x67c8(%rip)        # 8f90 <error@GLIBC_2.2.5>
    27c8:	8b 3d 4a 68 00 00    	mov    0x684a(%rip),%edi        # 9018 <__progname@@GLIBC_2.2.5-0x68>
    27ce:	ff 15 d4 66 00 00    	callq  *0x66d4(%rip)        # 8ea8 <_exit@GLIBC_2.2.5>
    27d4:	48 89 c1             	mov    %rax,%rcx
    27d7:	48 8d 15 f7 3a 00 00 	lea    0x3af7(%rip),%rdx        # 62d5 <__progname@@GLIBC_2.2.5-0x2dab>
    27de:	8b 33                	mov    (%rbx),%esi
    27e0:	31 ff                	xor    %edi,%edi
    27e2:	31 c0                	xor    %eax,%eax
    27e4:	ff 15 a6 67 00 00    	callq  *0x67a6(%rip)        # 8f90 <error@GLIBC_2.2.5>
    27ea:	eb dc                	jmp    27c8 <__progname@@GLIBC_2.2.5-0x68b8>
    27ec:	0f 1f 40 00          	nopl   0x0(%rax)
    27f0:	41 55                	push   %r13
    27f2:	41 54                	push   %r12
    27f4:	55                   	push   %rbp
    27f5:	53                   	push   %rbx
    27f6:	48 83 ec 08          	sub    $0x8,%rsp
    27fa:	48 85 d2             	test   %rdx,%rdx
    27fd:	74 63                	je     2862 <__progname@@GLIBC_2.2.5-0x681e>
    27ff:	41 89 fd             	mov    %edi,%r13d
    2802:	48 89 f5             	mov    %rsi,%rbp
    2805:	48 89 d3             	mov    %rdx,%rbx
    2808:	45 31 e4             	xor    %r12d,%r12d
    280b:	eb 13                	jmp    2820 <__progname@@GLIBC_2.2.5-0x6860>
    280d:	0f 1f 00             	nopl   (%rax)
    2810:	48 85 c0             	test   %rax,%rax
    2813:	74 33                	je     2848 <__progname@@GLIBC_2.2.5-0x6838>
    2815:	49 01 c4             	add    %rax,%r12
    2818:	48 01 c5             	add    %rax,%rbp
    281b:	48 29 c3             	sub    %rax,%rbx
    281e:	74 15                	je     2835 <__progname@@GLIBC_2.2.5-0x684b>
    2820:	48 89 da             	mov    %rbx,%rdx
    2823:	48 89 ee             	mov    %rbp,%rsi
    2826:	44 89 ef             	mov    %r13d,%edi
    2829:	67 e8 b1 1f 00 00    	addr32 callq 47e0 <__progname@@GLIBC_2.2.5-0x48a0>
    282f:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
    2833:	75 db                	jne    2810 <__progname@@GLIBC_2.2.5-0x6870>
    2835:	48 83 c4 08          	add    $0x8,%rsp
    2839:	4c 89 e0             	mov    %r12,%rax
    283c:	5b                   	pop    %rbx
    283d:	5d                   	pop    %rbp
    283e:	41 5c                	pop    %r12
    2840:	41 5d                	pop    %r13
    2842:	c3                   	retq   
    2843:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    2848:	ff 15 42 66 00 00    	callq  *0x6642(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    284e:	c7 00 1c 00 00 00    	movl   $0x1c,(%rax)
    2854:	48 83 c4 08          	add    $0x8,%rsp
    2858:	4c 89 e0             	mov    %r12,%rax
    285b:	5b                   	pop    %rbx
    285c:	5d                   	pop    %rbp
    285d:	41 5c                	pop    %r12
    285f:	41 5d                	pop    %r13
    2861:	c3                   	retq   
    2862:	45 31 e4             	xor    %r12d,%r12d
    2865:	eb ce                	jmp    2835 <__progname@@GLIBC_2.2.5-0x684b>
    2867:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    286e:	00 00 
    2870:	41 55                	push   %r13
    2872:	4d 89 c5             	mov    %r8,%r13
    2875:	41 54                	push   %r12
    2877:	49 89 cc             	mov    %rcx,%r12
    287a:	55                   	push   %rbp
    287b:	48 89 d5             	mov    %rdx,%rbp
    287e:	53                   	push   %rbx
    287f:	48 81 ec e8 00 00 00 	sub    $0xe8,%rsp
    2886:	84 c0                	test   %al,%al
    2888:	74 3a                	je     28c4 <__progname@@GLIBC_2.2.5-0x67bc>
    288a:	0f 29 44 24 60       	movaps %xmm0,0x60(%rsp)
    288f:	0f 29 4c 24 70       	movaps %xmm1,0x70(%rsp)
    2894:	0f 29 94 24 80 00 00 	movaps %xmm2,0x80(%rsp)
    289b:	00 
    289c:	0f 29 9c 24 90 00 00 	movaps %xmm3,0x90(%rsp)
    28a3:	00 
    28a4:	0f 29 a4 24 a0 00 00 	movaps %xmm4,0xa0(%rsp)
    28ab:	00 
    28ac:	0f 29 ac 24 b0 00 00 	movaps %xmm5,0xb0(%rsp)
    28b3:	00 
    28b4:	0f 29 b4 24 c0 00 00 	movaps %xmm6,0xc0(%rsp)
    28bb:	00 
    28bc:	0f 29 bc 24 d0 00 00 	movaps %xmm7,0xd0(%rsp)
    28c3:	00 
    28c4:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    28cb:	00 00 
    28cd:	48 89 44 24 28       	mov    %rax,0x28(%rsp)
    28d2:	31 c0                	xor    %eax,%eax
    28d4:	8b 1d c6 67 00 00    	mov    0x67c6(%rip),%ebx        # 90a0 <opterr@@GLIBC_2.2.5>
    28da:	c7 05 bc 67 00 00 00 	movl   $0x0,0x67bc(%rip)        # 90a0 <opterr@@GLIBC_2.2.5>
    28e1:	00 00 00 
    28e4:	83 ff 02             	cmp    $0x2,%edi
    28e7:	74 37                	je     2920 <__progname@@GLIBC_2.2.5-0x6760>
    28e9:	89 1d b1 67 00 00    	mov    %ebx,0x67b1(%rip)        # 90a0 <opterr@@GLIBC_2.2.5>
    28ef:	c7 05 97 67 00 00 00 	movl   $0x0,0x6797(%rip)        # 9090 <optind@@GLIBC_2.2.5>
    28f6:	00 00 00 
    28f9:	48 8b 44 24 28       	mov    0x28(%rsp),%rax
    28fe:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    2905:	00 00 
    2907:	0f 85 9d 00 00 00    	jne    29aa <__progname@@GLIBC_2.2.5-0x66d6>
    290d:	48 81 c4 e8 00 00 00 	add    $0xe8,%rsp
    2914:	5b                   	pop    %rbx
    2915:	5d                   	pop    %rbp
    2916:	41 5c                	pop    %r12
    2918:	41 5d                	pop    %r13
    291a:	c3                   	retq   
    291b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    2920:	45 31 c0             	xor    %r8d,%r8d
    2923:	4c 89 4c 24 08       	mov    %r9,0x8(%rsp)
    2928:	48 8d 0d d1 62 00 00 	lea    0x62d1(%rip),%rcx        # 8c00 <__progname@@GLIBC_2.2.5-0x480>
    292f:	48 8d 15 7c 37 00 00 	lea    0x377c(%rip),%rdx        # 60b2 <__progname@@GLIBC_2.2.5-0x2fce>
    2936:	ff 15 bc 65 00 00    	callq  *0x65bc(%rip)        # 8ef8 <getopt_long@GLIBC_2.2.5>
    293c:	83 f8 ff             	cmp    $0xffffffff,%eax
    293f:	74 a8                	je     28e9 <__progname@@GLIBC_2.2.5-0x6797>
    2941:	83 f8 68             	cmp    $0x68,%eax
    2944:	4c 8b 4c 24 08       	mov    0x8(%rsp),%r9
    2949:	74 55                	je     29a0 <__progname@@GLIBC_2.2.5-0x66e0>
    294b:	83 f8 76             	cmp    $0x76,%eax
    294e:	75 99                	jne    28e9 <__progname@@GLIBC_2.2.5-0x6797>
    2950:	48 8d 84 24 10 01 00 	lea    0x110(%rsp),%rax
    2957:	00 
    2958:	4c 8d 44 24 10       	lea    0x10(%rsp),%r8
    295d:	4c 89 e9             	mov    %r13,%rcx
    2960:	48 8b 3d 21 67 00 00 	mov    0x6721(%rip),%rdi        # 9088 <stdout@@GLIBC_2.2.5>
    2967:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    296c:	48 8d 44 24 30       	lea    0x30(%rsp),%rax
    2971:	4c 89 e2             	mov    %r12,%rdx
    2974:	48 89 ee             	mov    %rbp,%rsi
    2977:	c7 44 24 10 30 00 00 	movl   $0x30,0x10(%rsp)
    297e:	00 
    297f:	c7 44 24 14 30 00 00 	movl   $0x30,0x14(%rsp)
    2986:	00 
    2987:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
    298c:	67 e8 0e 23 00 00    	addr32 callq 4ca0 <__progname@@GLIBC_2.2.5-0x43e0>
    2992:	31 ff                	xor    %edi,%edi
    2994:	ff 15 0e 66 00 00    	callq  *0x660e(%rip)        # 8fa8 <exit@GLIBC_2.2.5>
    299a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    29a0:	31 ff                	xor    %edi,%edi
    29a2:	41 ff d1             	callq  *%r9
    29a5:	e9 3f ff ff ff       	jmpq   28e9 <__progname@@GLIBC_2.2.5-0x6797>
    29aa:	ff 15 40 65 00 00    	callq  *0x6540(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    29b0:	53                   	push   %rbx
    29b1:	48 85 ff             	test   %rdi,%rdi
    29b4:	74 78                	je     2a2e <__progname@@GLIBC_2.2.5-0x6652>
    29b6:	48 89 fb             	mov    %rdi,%rbx
    29b9:	be 2f 00 00 00       	mov    $0x2f,%esi
    29be:	ff 15 44 65 00 00    	callq  *0x6544(%rip)        # 8f08 <strrchr@GLIBC_2.2.5>
    29c4:	48 85 c0             	test   %rax,%rax
    29c7:	74 55                	je     2a1e <__progname@@GLIBC_2.2.5-0x6662>
    29c9:	4c 8d 40 01          	lea    0x1(%rax),%r8
    29cd:	4c 89 c2             	mov    %r8,%rdx
    29d0:	48 29 da             	sub    %rbx,%rdx
    29d3:	48 83 fa 06          	cmp    $0x6,%rdx
    29d7:	7e 45                	jle    2a1e <__progname@@GLIBC_2.2.5-0x6662>
    29d9:	48 8d 70 fa          	lea    -0x6(%rax),%rsi
    29dd:	b9 07 00 00 00       	mov    $0x7,%ecx
    29e2:	48 8d 3d 37 39 00 00 	lea    0x3937(%rip),%rdi        # 6320 <__progname@@GLIBC_2.2.5-0x2d60>
    29e9:	f3 a6                	repz cmpsb %es:(%rdi),%ds:(%rsi)
    29eb:	0f 97 c2             	seta   %dl
    29ee:	80 da 00             	sbb    $0x0,%dl
    29f1:	84 d2                	test   %dl,%dl
    29f3:	75 29                	jne    2a1e <__progname@@GLIBC_2.2.5-0x6662>
    29f5:	b9 03 00 00 00       	mov    $0x3,%ecx
    29fa:	48 8d 3d 27 39 00 00 	lea    0x3927(%rip),%rdi        # 6328 <__progname@@GLIBC_2.2.5-0x2d58>
    2a01:	4c 89 c6             	mov    %r8,%rsi
    2a04:	4c 89 c3             	mov    %r8,%rbx
    2a07:	f3 a6                	repz cmpsb %es:(%rdi),%ds:(%rsi)
    2a09:	0f 97 c2             	seta   %dl
    2a0c:	80 da 00             	sbb    $0x0,%dl
    2a0f:	84 d2                	test   %dl,%dl
    2a11:	75 0b                	jne    2a1e <__progname@@GLIBC_2.2.5-0x6662>
    2a13:	48 8d 58 04          	lea    0x4(%rax),%rbx
    2a17:	48 89 1d 62 66 00 00 	mov    %rbx,0x6662(%rip)        # 9080 <__progname@@GLIBC_2.2.5>
    2a1e:	48 89 1d bb 66 00 00 	mov    %rbx,0x66bb(%rip)        # 90e0 <stderr@@GLIBC_2.2.5+0x20>
    2a25:	48 89 1d 6c 66 00 00 	mov    %rbx,0x666c(%rip)        # 9098 <__progname_full@@GLIBC_2.2.5>
    2a2c:	5b                   	pop    %rbx
    2a2d:	c3                   	retq   
    2a2e:	48 8b 0d 8b 66 00 00 	mov    0x668b(%rip),%rcx        # 90c0 <stderr@@GLIBC_2.2.5>
    2a35:	ba 37 00 00 00       	mov    $0x37,%edx
    2a3a:	be 01 00 00 00       	mov    $0x1,%esi
    2a3f:	48 8d 3d a2 38 00 00 	lea    0x38a2(%rip),%rdi        # 62e8 <__progname@@GLIBC_2.2.5-0x2d98>
    2a46:	ff 15 64 65 00 00    	callq  *0x6564(%rip)        # 8fb0 <fwrite@GLIBC_2.2.5>
    2a4c:	ff 15 36 64 00 00    	callq  *0x6436(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    2a52:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    2a59:	00 00 00 
    2a5c:	0f 1f 40 00          	nopl   0x0(%rax)
    2a60:	41 54                	push   %r12
    2a62:	ba 05 00 00 00       	mov    $0x5,%edx
    2a67:	41 89 f4             	mov    %esi,%r12d
    2a6a:	48 89 fe             	mov    %rdi,%rsi
    2a6d:	55                   	push   %rbp
    2a6e:	48 89 fd             	mov    %rdi,%rbp
    2a71:	31 ff                	xor    %edi,%edi
    2a73:	53                   	push   %rbx
    2a74:	ff 15 5e 64 00 00    	callq  *0x645e(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    2a7a:	48 89 c3             	mov    %rax,%rbx
    2a7d:	48 39 c5             	cmp    %rax,%rbp
    2a80:	74 0e                	je     2a90 <__progname@@GLIBC_2.2.5-0x65f0>
    2a82:	48 89 d8             	mov    %rbx,%rax
    2a85:	5b                   	pop    %rbx
    2a86:	5d                   	pop    %rbp
    2a87:	41 5c                	pop    %r12
    2a89:	c3                   	retq   
    2a8a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    2a90:	67 e8 0a 28 00 00    	addr32 callq 52a0 <__progname@@GLIBC_2.2.5-0x3de0>
    2a96:	0f b6 10             	movzbl (%rax),%edx
    2a99:	83 e2 df             	and    $0xffffffdf,%edx
    2a9c:	80 fa 55             	cmp    $0x55,%dl
    2a9f:	75 47                	jne    2ae8 <__progname@@GLIBC_2.2.5-0x6598>
    2aa1:	0f b6 50 01          	movzbl 0x1(%rax),%edx
    2aa5:	83 e2 df             	and    $0xffffffdf,%edx
    2aa8:	80 fa 54             	cmp    $0x54,%dl
    2aab:	0f 85 7f 00 00 00    	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2ab1:	0f b6 50 02          	movzbl 0x2(%rax),%edx
    2ab5:	83 e2 df             	and    $0xffffffdf,%edx
    2ab8:	80 fa 46             	cmp    $0x46,%dl
    2abb:	75 73                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2abd:	80 78 03 2d          	cmpb   $0x2d,0x3(%rax)
    2ac1:	75 6d                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2ac3:	80 78 04 38          	cmpb   $0x38,0x4(%rax)
    2ac7:	75 67                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2ac9:	80 78 05 00          	cmpb   $0x0,0x5(%rax)
    2acd:	75 61                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2acf:	80 3b 60             	cmpb   $0x60,(%rbx)
    2ad2:	0f 84 78 00 00 00    	je     2b50 <__progname@@GLIBC_2.2.5-0x6530>
    2ad8:	48 8d 1d 4f 38 00 00 	lea    0x384f(%rip),%rbx        # 632e <__progname@@GLIBC_2.2.5-0x2d52>
    2adf:	eb a1                	jmp    2a82 <__progname@@GLIBC_2.2.5-0x65fe>
    2ae1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    2ae8:	80 fa 47             	cmp    $0x47,%dl
    2aeb:	75 43                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2aed:	0f b6 50 01          	movzbl 0x1(%rax),%edx
    2af1:	83 e2 df             	and    $0xffffffdf,%edx
    2af4:	80 fa 42             	cmp    $0x42,%dl
    2af7:	75 37                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2af9:	80 78 02 31          	cmpb   $0x31,0x2(%rax)
    2afd:	75 31                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2aff:	80 78 03 38          	cmpb   $0x38,0x3(%rax)
    2b03:	75 2b                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2b05:	80 78 04 30          	cmpb   $0x30,0x4(%rax)
    2b09:	75 25                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2b0b:	80 78 05 33          	cmpb   $0x33,0x5(%rax)
    2b0f:	75 1f                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2b11:	80 78 06 30          	cmpb   $0x30,0x6(%rax)
    2b15:	75 19                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2b17:	80 78 07 00          	cmpb   $0x0,0x7(%rax)
    2b1b:	75 13                	jne    2b30 <__progname@@GLIBC_2.2.5-0x6550>
    2b1d:	80 3b 60             	cmpb   $0x60,(%rbx)
    2b20:	74 3e                	je     2b60 <__progname@@GLIBC_2.2.5-0x6520>
    2b22:	48 8d 1d 09 38 00 00 	lea    0x3809(%rip),%rbx        # 6332 <__progname@@GLIBC_2.2.5-0x2d4e>
    2b29:	e9 54 ff ff ff       	jmpq   2a82 <__progname@@GLIBC_2.2.5-0x65fe>
    2b2e:	66 90                	xchg   %ax,%ax
    2b30:	41 83 fc 09          	cmp    $0x9,%r12d
    2b34:	48 8d 05 02 38 00 00 	lea    0x3802(%rip),%rax        # 633d <__progname@@GLIBC_2.2.5-0x2d43>
    2b3b:	48 8d 1d ea 37 00 00 	lea    0x37ea(%rip),%rbx        # 632c <__progname@@GLIBC_2.2.5-0x2d54>
    2b42:	48 0f 45 d8          	cmovne %rax,%rbx
    2b46:	48 89 d8             	mov    %rbx,%rax
    2b49:	5b                   	pop    %rbx
    2b4a:	5d                   	pop    %rbp
    2b4b:	41 5c                	pop    %r12
    2b4d:	c3                   	retq   
    2b4e:	66 90                	xchg   %ax,%ax
    2b50:	48 8d 1d e2 37 00 00 	lea    0x37e2(%rip),%rbx        # 6339 <__progname@@GLIBC_2.2.5-0x2d47>
    2b57:	e9 26 ff ff ff       	jmpq   2a82 <__progname@@GLIBC_2.2.5-0x65fe>
    2b5c:	0f 1f 40 00          	nopl   0x0(%rax)
    2b60:	48 8d 1d ce 37 00 00 	lea    0x37ce(%rip),%rbx        # 6335 <__progname@@GLIBC_2.2.5-0x2d4b>
    2b67:	e9 16 ff ff ff       	jmpq   2a82 <__progname@@GLIBC_2.2.5-0x65fe>
    2b6c:	0f 1f 40 00          	nopl   0x0(%rax)
    2b70:	41 57                	push   %r15
    2b72:	41 56                	push   %r14
    2b74:	49 89 fe             	mov    %rdi,%r14
    2b77:	41 55                	push   %r13
    2b79:	41 54                	push   %r12
    2b7b:	49 89 f4             	mov    %rsi,%r12
    2b7e:	55                   	push   %rbp
    2b7f:	48 89 cd             	mov    %rcx,%rbp
    2b82:	53                   	push   %rbx
    2b83:	44 89 cb             	mov    %r9d,%ebx
    2b86:	48 81 ec c8 00 00 00 	sub    $0xc8,%rsp
    2b8d:	48 8b 84 24 00 01 00 	mov    0x100(%rsp),%rax
    2b94:	00 
    2b95:	48 89 54 24 10       	mov    %rdx,0x10(%rsp)
    2b9a:	44 89 44 24 08       	mov    %r8d,0x8(%rsp)
    2b9f:	48 89 44 24 20       	mov    %rax,0x20(%rsp)
    2ba4:	48 8b 84 24 08 01 00 	mov    0x108(%rsp),%rax
    2bab:	00 
    2bac:	44 89 8c 24 88 00 00 	mov    %r9d,0x88(%rsp)
    2bb3:	00 
    2bb4:	48 89 44 24 68       	mov    %rax,0x68(%rsp)
    2bb9:	48 8b 84 24 10 01 00 	mov    0x110(%rsp),%rax
    2bc0:	00 
    2bc1:	48 89 44 24 60       	mov    %rax,0x60(%rsp)
    2bc6:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    2bcd:	00 00 
    2bcf:	48 89 84 24 b8 00 00 	mov    %rax,0xb8(%rsp)
    2bd6:	00 
    2bd7:	31 c0                	xor    %eax,%eax
    2bd9:	ff 15 01 63 00 00    	callq  *0x6301(%rip)        # 8ee0 <__ctype_get_mb_cur_max@GLIBC_2.2.5>
    2bdf:	44 8b 5c 24 08       	mov    0x8(%rsp),%r11d
    2be4:	83 e3 02             	and    $0x2,%ebx
    2be7:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
    2bec:	0f 95 44 24 43       	setne  0x43(%rsp)
    2bf1:	41 83 fb 0a          	cmp    $0xa,%r11d
    2bf5:	0f 87 25 f4 ff ff    	ja     2020 <__progname@@GLIBC_2.2.5-0x7060>
    2bfb:	48 8d 0d 9e 37 00 00 	lea    0x379e(%rip),%rcx        # 63a0 <__progname@@GLIBC_2.2.5-0x2ce0>
    2c02:	44 89 da             	mov    %r11d,%edx
    2c05:	48 63 04 91          	movslq (%rcx,%rdx,4),%rax
    2c09:	48 01 c8             	add    %rcx,%rax
    2c0c:	ff e0                	jmpq   *%rax
    2c0e:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    2c13:	45 31 ed             	xor    %r13d,%r13d
    2c16:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    2c1d:	00 
    2c1e:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    2c25:	00 00 
    2c27:	c6 44 24 43 01       	movb   $0x1,0x43(%rsp)
    2c2c:	c6 44 24 08 00       	movb   $0x0,0x8(%rsp)
    2c31:	48 8d 05 05 37 00 00 	lea    0x3705(%rip),%rax        # 633d <__progname@@GLIBC_2.2.5-0x2d43>
    2c38:	45 31 ff             	xor    %r15d,%r15d
    2c3b:	41 bb 02 00 00 00    	mov    $0x2,%r11d
    2c41:	48 c7 44 24 18 01 00 	movq   $0x1,0x18(%rsp)
    2c48:	00 00 
    2c4a:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    2c4f:	45 31 d2             	xor    %r10d,%r10d
    2c52:	44 89 d8             	mov    %r11d,%eax
    2c55:	45 89 e8             	mov    %r13d,%r8d
    2c58:	49 89 eb             	mov    %rbp,%r11
    2c5b:	4c 89 d5             	mov    %r10,%rbp
    2c5e:	41 89 c2             	mov    %eax,%r10d
    2c61:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    2c68:	49 39 eb             	cmp    %rbp,%r11
    2c6b:	41 0f 95 c5          	setne  %r13b
    2c6f:	49 83 fb ff          	cmp    $0xffffffffffffffff,%r11
    2c73:	75 0d                	jne    2c82 <__progname@@GLIBC_2.2.5-0x63fe>
    2c75:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    2c7a:	80 3c 28 00          	cmpb   $0x0,(%rax,%rbp,1)
    2c7e:	41 0f 95 c5          	setne  %r13b
    2c82:	45 84 ed             	test   %r13b,%r13b
    2c85:	0f 84 5d 07 00 00    	je     33e8 <__progname@@GLIBC_2.2.5-0x5c98>
    2c8b:	41 83 fa 02          	cmp    $0x2,%r10d
    2c8f:	48 8b 7c 24 10       	mov    0x10(%rsp),%rdi
    2c94:	0f 95 c0             	setne  %al
    2c97:	22 44 24 08          	and    0x8(%rsp),%al
    2c9b:	4c 8d 0c 2f          	lea    (%rdi,%rbp,1),%r9
    2c9f:	88 44 24 0c          	mov    %al,0xc(%rsp)
    2ca3:	0f 84 27 05 00 00    	je     31d0 <__progname@@GLIBC_2.2.5-0x5eb0>
    2ca9:	48 8b 44 24 18       	mov    0x18(%rsp),%rax
    2cae:	48 85 c0             	test   %rax,%rax
    2cb1:	0f 84 a9 06 00 00    	je     3360 <__progname@@GLIBC_2.2.5-0x5d20>
    2cb7:	48 8d 5c 05 00       	lea    0x0(%rbp,%rax,1),%rbx
    2cbc:	49 83 fb ff          	cmp    $0xffffffffffffffff,%r11
    2cc0:	75 2e                	jne    2cf0 <__progname@@GLIBC_2.2.5-0x6390>
    2cc2:	48 83 f8 01          	cmp    $0x1,%rax
    2cc6:	76 28                	jbe    2cf0 <__progname@@GLIBC_2.2.5-0x6390>
    2cc8:	44 89 54 24 38       	mov    %r10d,0x38(%rsp)
    2ccd:	44 88 44 24 30       	mov    %r8b,0x30(%rsp)
    2cd2:	4c 89 4c 24 28       	mov    %r9,0x28(%rsp)
    2cd7:	ff 15 0b 62 00 00    	callq  *0x620b(%rip)        # 8ee8 <strlen@GLIBC_2.2.5>
    2cdd:	44 8b 54 24 38       	mov    0x38(%rsp),%r10d
    2ce2:	44 0f b6 44 24 30    	movzbl 0x30(%rsp),%r8d
    2ce8:	4c 8b 4c 24 28       	mov    0x28(%rsp),%r9
    2ced:	49 89 c3             	mov    %rax,%r11
    2cf0:	4c 39 db             	cmp    %r11,%rbx
    2cf3:	0f 87 67 06 00 00    	ja     3360 <__progname@@GLIBC_2.2.5-0x5d20>
    2cf9:	44 89 54 24 44       	mov    %r10d,0x44(%rsp)
    2cfe:	4c 89 cf             	mov    %r9,%rdi
    2d01:	48 8b 54 24 18       	mov    0x18(%rsp),%rdx
    2d06:	4c 89 5c 24 38       	mov    %r11,0x38(%rsp)
    2d0b:	48 8b 74 24 48       	mov    0x48(%rsp),%rsi
    2d10:	44 88 44 24 30       	mov    %r8b,0x30(%rsp)
    2d15:	4c 89 4c 24 28       	mov    %r9,0x28(%rsp)
    2d1a:	ff 15 08 62 00 00    	callq  *0x6208(%rip)        # 8f28 <memcmp@GLIBC_2.2.5>
    2d20:	4c 8b 4c 24 28       	mov    0x28(%rsp),%r9
    2d25:	44 0f b6 44 24 30    	movzbl 0x30(%rsp),%r8d
    2d2b:	85 c0                	test   %eax,%eax
    2d2d:	4c 8b 5c 24 38       	mov    0x38(%rsp),%r11
    2d32:	44 8b 54 24 44       	mov    0x44(%rsp),%r10d
    2d37:	0f 85 23 06 00 00    	jne    3360 <__progname@@GLIBC_2.2.5-0x5d20>
    2d3d:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    2d42:	0f 85 f3 0f 00 00    	jne    3d3b <__progname@@GLIBC_2.2.5-0x5345>
    2d48:	41 0f b6 19          	movzbl (%r9),%ebx
    2d4c:	80 fb 7e             	cmp    $0x7e,%bl
    2d4f:	0f 87 18 04 00 00    	ja     316d <__progname@@GLIBC_2.2.5-0x5f13>
    2d55:	48 8d 0d 70 36 00 00 	lea    0x3670(%rip),%rcx        # 63cc <__progname@@GLIBC_2.2.5-0x2cb4>
    2d5c:	0f b6 d3             	movzbl %bl,%edx
    2d5f:	48 63 04 91          	movslq (%rcx,%rdx,4),%rax
    2d63:	48 01 c8             	add    %rcx,%rax
    2d66:	ff e0                	jmpq   *%rax
    2d68:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    2d6f:	00 
    2d70:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    2d75:	49 83 fb 01          	cmp    $0x1,%r11
    2d79:	0f 95 c0             	setne  %al
    2d7c:	49 83 fb ff          	cmp    $0xffffffffffffffff,%r11
    2d80:	75 0c                	jne    2d8e <__progname@@GLIBC_2.2.5-0x62f2>
    2d82:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    2d87:	80 78 01 00          	cmpb   $0x0,0x1(%rax)
    2d8b:	0f 95 c0             	setne  %al
    2d8e:	41 83 fa 02          	cmp    $0x2,%r10d
    2d92:	0f 94 c2             	sete   %dl
    2d95:	84 c0                	test   %al,%al
    2d97:	0f 85 06 02 00 00    	jne    2fa3 <__progname@@GLIBC_2.2.5-0x60dd>
    2d9d:	48 85 ed             	test   %rbp,%rbp
    2da0:	0f 85 fd 01 00 00    	jne    2fa3 <__progname@@GLIBC_2.2.5-0x60dd>
    2da6:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    2dab:	74 0b                	je     2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    2dad:	84 d2                	test   %dl,%dl
    2daf:	0f 85 5d 04 00 00    	jne    3212 <__progname@@GLIBC_2.2.5-0x5e6e>
    2db5:	0f 1f 00             	nopl   (%rax)
    2db8:	0f b6 44 24 08       	movzbl 0x8(%rsp),%eax
    2dbd:	83 f0 01             	xor    $0x1,%eax
    2dc0:	09 d0                	or     %edx,%eax
    2dc2:	83 f0 01             	xor    $0x1,%eax
    2dc5:	0a 44 24 43          	or     0x43(%rsp),%al
    2dc9:	0f 84 f1 00 00 00    	je     2ec0 <__progname@@GLIBC_2.2.5-0x61c0>
    2dcf:	31 c0                	xor    %eax,%eax
    2dd1:	48 8b 74 24 20       	mov    0x20(%rsp),%rsi
    2dd6:	48 85 f6             	test   %rsi,%rsi
    2dd9:	0f 84 e1 00 00 00    	je     2ec0 <__progname@@GLIBC_2.2.5-0x61c0>
    2ddf:	89 da                	mov    %ebx,%edx
    2de1:	89 d9                	mov    %ebx,%ecx
    2de3:	c0 ea 05             	shr    $0x5,%dl
    2de6:	0f b6 d2             	movzbl %dl,%edx
    2de9:	8b 14 96             	mov    (%rsi,%rdx,4),%edx
    2dec:	d3 ea                	shr    %cl,%edx
    2dee:	83 e2 01             	and    $0x1,%edx
    2df1:	0f 84 c9 00 00 00    	je     2ec0 <__progname@@GLIBC_2.2.5-0x61c0>
    2df7:	41 83 fa 02          	cmp    $0x2,%r10d
    2dfb:	0f 94 c2             	sete   %dl
    2dfe:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    2e03:	0f 85 bf 01 00 00    	jne    2fc8 <__progname@@GLIBC_2.2.5-0x60b8>
    2e09:	44 89 c0             	mov    %r8d,%eax
    2e0c:	83 f0 01             	xor    $0x1,%eax
    2e0f:	20 d0                	and    %dl,%al
    2e11:	74 2f                	je     2e42 <__progname@@GLIBC_2.2.5-0x623e>
    2e13:	4d 39 fc             	cmp    %r15,%r12
    2e16:	76 05                	jbe    2e1d <__progname@@GLIBC_2.2.5-0x6263>
    2e18:	43 c6 04 3e 27       	movb   $0x27,(%r14,%r15,1)
    2e1d:	49 8d 57 01          	lea    0x1(%r15),%rdx
    2e21:	4c 39 e2             	cmp    %r12,%rdx
    2e24:	73 06                	jae    2e2c <__progname@@GLIBC_2.2.5-0x6254>
    2e26:	43 c6 44 3e 01 24    	movb   $0x24,0x1(%r14,%r15,1)
    2e2c:	49 8d 57 02          	lea    0x2(%r15),%rdx
    2e30:	4c 39 e2             	cmp    %r12,%rdx
    2e33:	73 06                	jae    2e3b <__progname@@GLIBC_2.2.5-0x6245>
    2e35:	43 c6 44 3e 02 27    	movb   $0x27,0x2(%r14,%r15,1)
    2e3b:	49 83 c7 03          	add    $0x3,%r15
    2e3f:	41 89 c0             	mov    %eax,%r8d
    2e42:	4d 39 fc             	cmp    %r15,%r12
    2e45:	76 05                	jbe    2e4c <__progname@@GLIBC_2.2.5-0x6234>
    2e47:	43 c6 04 3e 5c       	movb   $0x5c,(%r14,%r15,1)
    2e4c:	49 83 c7 01          	add    $0x1,%r15
    2e50:	48 83 c5 01          	add    $0x1,%rbp
    2e54:	4d 39 e7             	cmp    %r12,%r15
    2e57:	73 04                	jae    2e5d <__progname@@GLIBC_2.2.5-0x6223>
    2e59:	43 88 1c 3e          	mov    %bl,(%r14,%r15,1)
    2e5d:	0f b6 7c 24 42       	movzbl 0x42(%rsp),%edi
    2e62:	49 83 c7 01          	add    $0x1,%r15
    2e66:	b8 00 00 00 00       	mov    $0x0,%eax
    2e6b:	45 84 ed             	test   %r13b,%r13b
    2e6e:	0f 44 f8             	cmove  %eax,%edi
    2e71:	40 88 7c 24 42       	mov    %dil,0x42(%rsp)
    2e76:	e9 ed fd ff ff       	jmpq   2c68 <__progname@@GLIBC_2.2.5-0x6418>
    2e7b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    2e80:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    2e85:	0f 85 a5 0e 00 00    	jne    3d30 <__progname@@GLIBC_2.2.5-0x5350>
    2e8b:	4d 85 e4             	test   %r12,%r12
    2e8e:	0f 84 08 08 00 00    	je     369c <__progname@@GLIBC_2.2.5-0x59e4>
    2e94:	31 d2                	xor    %edx,%edx
    2e96:	48 83 7c 24 50 00    	cmpq   $0x0,0x50(%rsp)
    2e9c:	0f 85 fa 07 00 00    	jne    369c <__progname@@GLIBC_2.2.5-0x59e4>
    2ea2:	4c 89 64 24 50       	mov    %r12,0x50(%rsp)
    2ea7:	49 83 c7 03          	add    $0x3,%r15
    2eab:	31 c0                	xor    %eax,%eax
    2ead:	45 31 c0             	xor    %r8d,%r8d
    2eb0:	44 88 ac 24 8d 00 00 	mov    %r13b,0x8d(%rsp)
    2eb7:	00 
    2eb8:	49 89 d4             	mov    %rdx,%r12
    2ebb:	bb 27 00 00 00       	mov    $0x27,%ebx
    2ec0:	41 83 fa 02          	cmp    $0x2,%r10d
    2ec4:	0f 94 c2             	sete   %dl
    2ec7:	80 7c 24 0c 00       	cmpb   $0x0,0xc(%rsp)
    2ecc:	0f 85 2c ff ff ff    	jne    2dfe <__progname@@GLIBC_2.2.5-0x6282>
    2ed2:	83 f0 01             	xor    $0x1,%eax
    2ed5:	48 83 c5 01          	add    $0x1,%rbp
    2ed9:	44 21 c0             	and    %r8d,%eax
    2edc:	84 c0                	test   %al,%al
    2ede:	0f 84 70 ff ff ff    	je     2e54 <__progname@@GLIBC_2.2.5-0x622c>
    2ee4:	4d 39 fc             	cmp    %r15,%r12
    2ee7:	76 05                	jbe    2eee <__progname@@GLIBC_2.2.5-0x6192>
    2ee9:	43 c6 04 3e 27       	movb   $0x27,(%r14,%r15,1)
    2eee:	49 8d 47 01          	lea    0x1(%r15),%rax
    2ef2:	49 39 c4             	cmp    %rax,%r12
    2ef5:	76 06                	jbe    2efd <__progname@@GLIBC_2.2.5-0x6183>
    2ef7:	43 c6 44 3e 01 27    	movb   $0x27,0x1(%r14,%r15,1)
    2efd:	49 83 c7 02          	add    $0x2,%r15
    2f01:	45 31 c0             	xor    %r8d,%r8d
    2f04:	e9 4b ff ff ff       	jmpq   2e54 <__progname@@GLIBC_2.2.5-0x622c>
    2f09:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    2f10:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    2f15:	41 83 fa 02          	cmp    $0x2,%r10d
    2f19:	0f 84 a1 05 00 00    	je     34c0 <__progname@@GLIBC_2.2.5-0x5bc0>
    2f1f:	41 83 fa 05          	cmp    $0x5,%r10d
    2f23:	0f 84 57 05 00 00    	je     3480 <__progname@@GLIBC_2.2.5-0x5c00>
    2f29:	41 83 fa 02          	cmp    $0x2,%r10d
    2f2d:	bb 3f 00 00 00       	mov    $0x3f,%ebx
    2f32:	0f 94 c2             	sete   %dl
    2f35:	45 31 ed             	xor    %r13d,%r13d
    2f38:	e9 7b fe ff ff       	jmpq   2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    2f3d:	0f 1f 00             	nopl   (%rax)
    2f40:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    2f45:	41 83 fa 02          	cmp    $0x2,%r10d
    2f49:	0f 84 31 ff ff ff    	je     2e80 <__progname@@GLIBC_2.2.5-0x6200>
    2f4f:	44 88 ac 24 8d 00 00 	mov    %r13b,0x8d(%rsp)
    2f56:	00 
    2f57:	31 d2                	xor    %edx,%edx
    2f59:	bb 27 00 00 00       	mov    $0x27,%ebx
    2f5e:	e9 55 fe ff ff       	jmpq   2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    2f63:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    2f68:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    2f6d:	0f b6 54 24 08       	movzbl 0x8(%rsp),%edx
    2f72:	22 54 24 43          	and    0x43(%rsp),%dl
    2f76:	bb 5c 00 00 00       	mov    $0x5c,%ebx
    2f7b:	b9 5c 00 00 00       	mov    $0x5c,%ecx
    2f80:	48 83 7c 24 18 00    	cmpq   $0x0,0x18(%rsp)
    2f86:	0f 95 c0             	setne  %al
    2f89:	20 c2                	and    %al,%dl
    2f8b:	0f 85 5a 0b 00 00    	jne    3aeb <__progname@@GLIBC_2.2.5-0x5595>
    2f91:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    2f98:	80 7c 24 08 00       	cmpb   $0x0,0x8(%rsp)
    2f9d:	0f 85 b4 0e 00 00    	jne    3e57 <__progname@@GLIBC_2.2.5-0x5229>
    2fa3:	45 31 ed             	xor    %r13d,%r13d
    2fa6:	e9 0d fe ff ff       	jmpq   2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    2fab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    2fb0:	bb 6e 00 00 00       	mov    $0x6e,%ebx
    2fb5:	31 d2                	xor    %edx,%edx
    2fb7:	45 31 ed             	xor    %r13d,%r13d
    2fba:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    2fbf:	0f 84 44 fe ff ff    	je     2e09 <__progname@@GLIBC_2.2.5-0x6277>
    2fc5:	0f 1f 00             	nopl   (%rax)
    2fc8:	4c 89 dd             	mov    %r11,%rbp
    2fcb:	89 d0                	mov    %edx,%eax
    2fcd:	45 89 d3             	mov    %r10d,%r11d
    2fd0:	20 44 24 08          	and    %al,0x8(%rsp)
    2fd4:	80 7c 24 08 00       	cmpb   $0x0,0x8(%rsp)
    2fd9:	b8 04 00 00 00       	mov    $0x4,%eax
    2fde:	44 0f 45 d8          	cmovne %eax,%r11d
    2fe2:	48 83 ec 08          	sub    $0x8,%rsp
    2fe6:	45 89 d8             	mov    %r11d,%r8d
    2fe9:	48 89 e9             	mov    %rbp,%rcx
    2fec:	ff 74 24 68          	pushq  0x68(%rsp)
    2ff0:	4c 89 e6             	mov    %r12,%rsi
    2ff3:	4c 89 f7             	mov    %r14,%rdi
    2ff6:	ff 74 24 78          	pushq  0x78(%rsp)
    2ffa:	6a 00                	pushq  $0x0
    2ffc:	44 8b 8c 24 a8 00 00 	mov    0xa8(%rsp),%r9d
    3003:	00 
    3004:	48 8b 54 24 30       	mov    0x30(%rsp),%rdx
    3009:	41 83 e1 fd          	and    $0xfffffffd,%r9d
    300d:	e8 5e fb ff ff       	callq  2b70 <__progname@@GLIBC_2.2.5-0x6510>
    3012:	48 83 c4 20          	add    $0x20,%rsp
    3016:	49 89 c7             	mov    %rax,%r15
    3019:	48 8b 9c 24 b8 00 00 	mov    0xb8(%rsp),%rbx
    3020:	00 
    3021:	64 48 33 1c 25 28 00 	xor    %fs:0x28,%rbx
    3028:	00 00 
    302a:	4c 89 f8             	mov    %r15,%rax
    302d:	0f 85 c6 0d 00 00    	jne    3df9 <__progname@@GLIBC_2.2.5-0x5287>
    3033:	48 81 c4 c8 00 00 00 	add    $0xc8,%rsp
    303a:	5b                   	pop    %rbx
    303b:	5d                   	pop    %rbp
    303c:	41 5c                	pop    %r12
    303e:	41 5d                	pop    %r13
    3040:	41 5e                	pop    %r14
    3042:	41 5f                	pop    %r15
    3044:	c3                   	retq   
    3045:	0f 1f 00             	nopl   (%rax)
    3048:	bb 74 00 00 00       	mov    $0x74,%ebx
    304d:	e9 63 ff ff ff       	jmpq   2fb5 <__progname@@GLIBC_2.2.5-0x60cb>
    3052:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    3058:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    305d:	31 d2                	xor    %edx,%edx
    305f:	e9 3f ff ff ff       	jmpq   2fa3 <__progname@@GLIBC_2.2.5-0x60dd>
    3064:	0f 1f 40 00          	nopl   0x0(%rax)
    3068:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    306d:	41 83 fa 02          	cmp    $0x2,%r10d
    3071:	bb 0d 00 00 00       	mov    $0xd,%ebx
    3076:	b9 72 00 00 00       	mov    $0x72,%ecx
    307b:	0f 94 c2             	sete   %dl
    307e:	e9 15 ff ff ff       	jmpq   2f98 <__progname@@GLIBC_2.2.5-0x60e8>
    3083:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    3088:	bb 66 00 00 00       	mov    $0x66,%ebx
    308d:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    3092:	0f 85 4b 0c 00 00    	jne    3ce3 <__progname@@GLIBC_2.2.5-0x539d>
    3098:	45 31 ed             	xor    %r13d,%r13d
    309b:	e9 a2 fd ff ff       	jmpq   2e42 <__progname@@GLIBC_2.2.5-0x623e>
    30a0:	bb 76 00 00 00       	mov    $0x76,%ebx
    30a5:	eb e6                	jmp    308d <__progname@@GLIBC_2.2.5-0x5ff3>
    30a7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    30ae:	00 00 
    30b0:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    30b5:	0f 85 d3 0c 00 00    	jne    3d8e <__progname@@GLIBC_2.2.5-0x52f2>
    30bb:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    30c0:	41 83 fa 02          	cmp    $0x2,%r10d
    30c4:	44 89 c0             	mov    %r8d,%eax
    30c7:	0f 94 c2             	sete   %dl
    30ca:	83 f0 01             	xor    $0x1,%eax
    30cd:	20 d0                	and    %dl,%al
    30cf:	0f 84 b3 05 00 00    	je     3688 <__progname@@GLIBC_2.2.5-0x59f8>
    30d5:	4d 39 fc             	cmp    %r15,%r12
    30d8:	76 05                	jbe    30df <__progname@@GLIBC_2.2.5-0x5fa1>
    30da:	43 c6 04 3e 27       	movb   $0x27,(%r14,%r15,1)
    30df:	49 8d 4f 01          	lea    0x1(%r15),%rcx
    30e3:	49 39 cc             	cmp    %rcx,%r12
    30e6:	76 06                	jbe    30ee <__progname@@GLIBC_2.2.5-0x5f92>
    30e8:	43 c6 44 3e 01 24    	movb   $0x24,0x1(%r14,%r15,1)
    30ee:	49 8d 4f 02          	lea    0x2(%r15),%rcx
    30f2:	49 39 cc             	cmp    %rcx,%r12
    30f5:	76 06                	jbe    30fd <__progname@@GLIBC_2.2.5-0x5f83>
    30f7:	43 c6 44 3e 02 27    	movb   $0x27,0x2(%r14,%r15,1)
    30fd:	49 8d 4f 03          	lea    0x3(%r15),%rcx
    3101:	49 39 cc             	cmp    %rcx,%r12
    3104:	0f 86 26 07 00 00    	jbe    3830 <__progname@@GLIBC_2.2.5-0x5850>
    310a:	41 c6 04 0e 5c       	movb   $0x5c,(%r14,%rcx,1)
    310f:	41 89 c0             	mov    %eax,%r8d
    3112:	4c 8d 79 01          	lea    0x1(%rcx),%r15
    3116:	41 83 fa 02          	cmp    $0x2,%r10d
    311a:	0f 84 50 0a 00 00    	je     3b70 <__progname@@GLIBC_2.2.5-0x5510>
    3120:	48 8d 45 01          	lea    0x1(%rbp),%rax
    3124:	bb 30 00 00 00       	mov    $0x30,%ebx
    3129:	4c 39 d8             	cmp    %r11,%rax
    312c:	73 19                	jae    3147 <__progname@@GLIBC_2.2.5-0x5f39>
    312e:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    3133:	0f b6 44 28 01       	movzbl 0x1(%rax,%rbp,1),%eax
    3138:	88 44 24 28          	mov    %al,0x28(%rsp)
    313c:	83 e8 30             	sub    $0x30,%eax
    313f:	3c 09                	cmp    $0x9,%al
    3141:	0f 86 5b 09 00 00    	jbe    3aa2 <__progname@@GLIBC_2.2.5-0x55de>
    3147:	0f b6 44 24 08       	movzbl 0x8(%rsp),%eax
    314c:	83 f0 01             	xor    $0x1,%eax
    314f:	08 d0                	or     %dl,%al
    3151:	44 89 e8             	mov    %r13d,%eax
    3154:	41 bd 00 00 00 00    	mov    $0x0,%r13d
    315a:	0f 84 71 fc ff ff    	je     2dd1 <__progname@@GLIBC_2.2.5-0x62af>
    3160:	e9 5b fd ff ff       	jmpq   2ec0 <__progname@@GLIBC_2.2.5-0x61c0>
    3165:	0f 1f 00             	nopl   (%rax)
    3168:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    316d:	48 83 7c 24 58 01    	cmpq   $0x1,0x58(%rsp)
    3173:	0f 85 67 03 00 00    	jne    34e0 <__progname@@GLIBC_2.2.5-0x5ba0>
    3179:	44 89 54 24 38       	mov    %r10d,0x38(%rsp)
    317e:	4c 89 5c 24 30       	mov    %r11,0x30(%rsp)
    3183:	44 88 44 24 28       	mov    %r8b,0x28(%rsp)
    3188:	ff 15 52 5e 00 00    	callq  *0x5e52(%rip)        # 8fe0 <__ctype_b_loc@GLIBC_2.3>
    318e:	0f b6 d3             	movzbl %bl,%edx
    3191:	44 0f b6 44 24 28    	movzbl 0x28(%rsp),%r8d
    3197:	4c 8b 5c 24 30       	mov    0x30(%rsp),%r11
    319c:	48 8b 00             	mov    (%rax),%rax
    319f:	44 8b 54 24 38       	mov    0x38(%rsp),%r10d
    31a4:	bf 01 00 00 00       	mov    $0x1,%edi
    31a9:	0f b7 04 50          	movzwl (%rax,%rdx,2),%eax
    31ad:	66 25 00 40          	and    $0x4000,%ax
    31b1:	41 0f 95 c5          	setne  %r13b
    31b5:	0f 94 c2             	sete   %dl
    31b8:	22 54 24 08          	and    0x8(%rsp),%dl
    31bc:	84 d2                	test   %dl,%dl
    31be:	0f 85 1a 05 00 00    	jne    36de <__progname@@GLIBC_2.2.5-0x59a2>
    31c4:	41 83 fa 02          	cmp    $0x2,%r10d
    31c8:	0f 94 c2             	sete   %dl
    31cb:	e9 e8 fb ff ff       	jmpq   2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    31d0:	41 0f b6 19          	movzbl (%r9),%ebx
    31d4:	80 fb 7e             	cmp    $0x7e,%bl
    31d7:	77 94                	ja     316d <__progname@@GLIBC_2.2.5-0x5f13>
    31d9:	48 8d 0d e8 33 00 00 	lea    0x33e8(%rip),%rcx        # 65c8 <__progname@@GLIBC_2.2.5-0x2ab8>
    31e0:	0f b6 d3             	movzbl %bl,%edx
    31e3:	48 63 04 91          	movslq (%rcx,%rdx,4),%rax
    31e7:	48 01 c8             	add    %rcx,%rax
    31ea:	ff e0                	jmpq   *%rax
    31ec:	0f 1f 40 00          	nopl   0x0(%rax)
    31f0:	bb 0a 00 00 00       	mov    $0xa,%ebx
    31f5:	b9 6e 00 00 00       	mov    $0x6e,%ecx
    31fa:	41 83 fa 02          	cmp    $0x2,%r10d
    31fe:	0f b6 44 24 43       	movzbl 0x43(%rsp),%eax
    3203:	0f 94 c2             	sete   %dl
    3206:	20 d0                	and    %dl,%al
    3208:	88 44 24 0c          	mov    %al,0xc(%rsp)
    320c:	0f 84 86 fd ff ff    	je     2f98 <__progname@@GLIBC_2.2.5-0x60e8>
    3212:	4c 89 dd             	mov    %r11,%rbp
    3215:	41 bb 02 00 00 00    	mov    $0x2,%r11d
    321b:	e9 b4 fd ff ff       	jmpq   2fd4 <__progname@@GLIBC_2.2.5-0x60ac>
    3220:	bb 09 00 00 00       	mov    $0x9,%ebx
    3225:	b9 74 00 00 00       	mov    $0x74,%ecx
    322a:	eb ce                	jmp    31fa <__progname@@GLIBC_2.2.5-0x5e86>
    322c:	0f 1f 40 00          	nopl   0x0(%rax)
    3230:	41 83 fa 02          	cmp    $0x2,%r10d
    3234:	bb 08 00 00 00       	mov    $0x8,%ebx
    3239:	b9 62 00 00 00       	mov    $0x62,%ecx
    323e:	0f 94 c2             	sete   %dl
    3241:	e9 52 fd ff ff       	jmpq   2f98 <__progname@@GLIBC_2.2.5-0x60e8>
    3246:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    324d:	00 00 00 
    3250:	41 83 fa 02          	cmp    $0x2,%r10d
    3254:	bb 07 00 00 00       	mov    $0x7,%ebx
    3259:	b9 61 00 00 00       	mov    $0x61,%ecx
    325e:	0f 94 c2             	sete   %dl
    3261:	e9 32 fd ff ff       	jmpq   2f98 <__progname@@GLIBC_2.2.5-0x60e8>
    3266:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    326d:	00 00 00 
    3270:	80 7c 24 08 00       	cmpb   $0x0,0x8(%rsp)
    3275:	0f 85 35 fe ff ff    	jne    30b0 <__progname@@GLIBC_2.2.5-0x5fd0>
    327b:	f6 84 24 88 00 00 00 	testb  $0x1,0x88(%rsp)
    3282:	01 
    3283:	0f 85 4c 04 00 00    	jne    36d5 <__progname@@GLIBC_2.2.5-0x59ab>
    3289:	41 83 fa 02          	cmp    $0x2,%r10d
    328d:	c6 44 24 0c 00       	movb   $0x0,0xc(%rsp)
    3292:	0f 94 c2             	sete   %dl
    3295:	45 31 ed             	xor    %r13d,%r13d
    3298:	31 db                	xor    %ebx,%ebx
    329a:	e9 19 fb ff ff       	jmpq   2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    329f:	90                   	nop
    32a0:	41 83 fa 02          	cmp    $0x2,%r10d
    32a4:	0f 85 c3 fc ff ff    	jne    2f6d <__progname@@GLIBC_2.2.5-0x6113>
    32aa:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    32af:	0f 85 7b 0a 00 00    	jne    3d30 <__progname@@GLIBC_2.2.5-0x5350>
    32b5:	48 83 c5 01          	add    $0x1,%rbp
    32b9:	44 89 c0             	mov    %r8d,%eax
    32bc:	45 31 ed             	xor    %r13d,%r13d
    32bf:	bb 5c 00 00 00       	mov    $0x5c,%ebx
    32c4:	e9 13 fc ff ff       	jmpq   2edc <__progname@@GLIBC_2.2.5-0x61a4>
    32c9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    32d0:	41 83 fa 02          	cmp    $0x2,%r10d
    32d4:	0f 94 c2             	sete   %dl
    32d7:	e9 c1 fa ff ff       	jmpq   2d9d <__progname@@GLIBC_2.2.5-0x62e3>
    32dc:	0f 1f 40 00          	nopl   0x0(%rax)
    32e0:	41 83 fa 02          	cmp    $0x2,%r10d
    32e4:	0f 94 c2             	sete   %dl
    32e7:	45 31 ed             	xor    %r13d,%r13d
    32ea:	e9 b7 fa ff ff       	jmpq   2da6 <__progname@@GLIBC_2.2.5-0x62da>
    32ef:	90                   	nop
    32f0:	41 83 fa 02          	cmp    $0x2,%r10d
    32f4:	bb 20 00 00 00       	mov    $0x20,%ebx
    32f9:	0f 94 c2             	sete   %dl
    32fc:	e9 a5 fa ff ff       	jmpq   2da6 <__progname@@GLIBC_2.2.5-0x62da>
    3301:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    3308:	bb 0d 00 00 00       	mov    $0xd,%ebx
    330d:	b9 72 00 00 00       	mov    $0x72,%ecx
    3312:	e9 e3 fe ff ff       	jmpq   31fa <__progname@@GLIBC_2.2.5-0x5e86>
    3317:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    331e:	00 00 
    3320:	41 83 fa 02          	cmp    $0x2,%r10d
    3324:	bb 0c 00 00 00       	mov    $0xc,%ebx
    3329:	b9 66 00 00 00       	mov    $0x66,%ecx
    332e:	0f 94 c2             	sete   %dl
    3331:	e9 62 fc ff ff       	jmpq   2f98 <__progname@@GLIBC_2.2.5-0x60e8>
    3336:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    333d:	00 00 00 
    3340:	41 83 fa 02          	cmp    $0x2,%r10d
    3344:	bb 0b 00 00 00       	mov    $0xb,%ebx
    3349:	b9 76 00 00 00       	mov    $0x76,%ecx
    334e:	0f 94 c2             	sete   %dl
    3351:	e9 42 fc ff ff       	jmpq   2f98 <__progname@@GLIBC_2.2.5-0x60e8>
    3356:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    335d:	00 00 00 
    3360:	41 0f b6 19          	movzbl (%r9),%ebx
    3364:	80 fb 7e             	cmp    $0x7e,%bl
    3367:	0f 87 fb fd ff ff    	ja     3168 <__progname@@GLIBC_2.2.5-0x5f18>
    336d:	48 8d 0d 50 34 00 00 	lea    0x3450(%rip),%rcx        # 67c4 <__progname@@GLIBC_2.2.5-0x28bc>
    3374:	0f b6 d3             	movzbl %bl,%edx
    3377:	48 63 04 91          	movslq (%rcx,%rdx,4),%rax
    337b:	48 01 c8             	add    %rcx,%rax
    337e:	ff e0                	jmpq   *%rax
    3380:	31 c0                	xor    %eax,%eax
    3382:	44 0f b6 6c 24 0c    	movzbl 0xc(%rsp),%r13d
    3388:	88 44 24 0c          	mov    %al,0xc(%rsp)
    338c:	31 c0                	xor    %eax,%eax
    338e:	e9 3e fa ff ff       	jmpq   2dd1 <__progname@@GLIBC_2.2.5-0x62af>
    3393:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    3398:	31 c0                	xor    %eax,%eax
    339a:	48 85 ed             	test   %rbp,%rbp
    339d:	0f 85 d5 02 00 00    	jne    3678 <__progname@@GLIBC_2.2.5-0x5a08>
    33a3:	44 0f b6 6c 24 0c    	movzbl 0xc(%rsp),%r13d
    33a9:	31 d2                	xor    %edx,%edx
    33ab:	88 44 24 0c          	mov    %al,0xc(%rsp)
    33af:	e9 04 fa ff ff       	jmpq   2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    33b4:	0f 1f 40 00          	nopl   0x0(%rax)
    33b8:	31 c0                	xor    %eax,%eax
    33ba:	bb 20 00 00 00       	mov    $0x20,%ebx
    33bf:	eb c1                	jmp    3382 <__progname@@GLIBC_2.2.5-0x5cfe>
    33c1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    33c8:	bb 62 00 00 00       	mov    $0x62,%ebx
    33cd:	e9 e3 fb ff ff       	jmpq   2fb5 <__progname@@GLIBC_2.2.5-0x60cb>
    33d2:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    33d8:	bb 61 00 00 00       	mov    $0x61,%ebx
    33dd:	e9 ab fc ff ff       	jmpq   308d <__progname@@GLIBC_2.2.5-0x5ff3>
    33e2:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    33e8:	41 83 fa 02          	cmp    $0x2,%r10d
    33ec:	45 89 c5             	mov    %r8d,%r13d
    33ef:	4c 89 dd             	mov    %r11,%rbp
    33f2:	0f 94 c2             	sete   %dl
    33f5:	4d 85 ff             	test   %r15,%r15
    33f8:	75 0a                	jne    3404 <__progname@@GLIBC_2.2.5-0x5c7c>
    33fa:	84 54 24 43          	test   %dl,0x43(%rsp)
    33fe:	0f 85 ea 09 00 00    	jne    3dee <__progname@@GLIBC_2.2.5-0x5292>
    3404:	0f b6 44 24 43       	movzbl 0x43(%rsp),%eax
    3409:	83 f0 01             	xor    $0x1,%eax
    340c:	20 c2                	and    %al,%dl
    340e:	0f 84 32 09 00 00    	je     3d46 <__progname@@GLIBC_2.2.5-0x533a>
    3414:	80 bc 24 8d 00 00 00 	cmpb   $0x0,0x8d(%rsp)
    341b:	00 
    341c:	0f 84 26 09 00 00    	je     3d48 <__progname@@GLIBC_2.2.5-0x5338>
    3422:	80 7c 24 42 00       	cmpb   $0x0,0x42(%rsp)
    3427:	0f 85 75 09 00 00    	jne    3da2 <__progname@@GLIBC_2.2.5-0x52de>
    342d:	4d 85 e4             	test   %r12,%r12
    3430:	0f 94 c0             	sete   %al
    3433:	48 83 7c 24 50 00    	cmpq   $0x0,0x50(%rsp)
    3439:	0f 95 c2             	setne  %dl
    343c:	20 d0                	and    %dl,%al
    343e:	0f 84 9d 09 00 00    	je     3de1 <__progname@@GLIBC_2.2.5-0x529f>
    3444:	4c 8b 64 24 50       	mov    0x50(%rsp),%r12
    3449:	41 c6 06 27          	movb   $0x27,(%r14)
    344d:	48 8d 1d e9 2e 00 00 	lea    0x2ee9(%rip),%rbx        # 633d <__progname@@GLIBC_2.2.5-0x2d43>
    3454:	41 bb 02 00 00 00    	mov    $0x2,%r11d
    345a:	41 bf 01 00 00 00    	mov    $0x1,%r15d
    3460:	48 89 5c 24 48       	mov    %rbx,0x48(%rsp)
    3465:	48 c7 44 24 18 01 00 	movq   $0x1,0x18(%rsp)
    346c:	00 00 
    346e:	c6 44 24 43 00       	movb   $0x0,0x43(%rsp)
    3473:	88 84 24 8d 00 00 00 	mov    %al,0x8d(%rsp)
    347a:	e9 d0 f7 ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    347f:	90                   	nop
    3480:	f6 84 24 88 00 00 00 	testb  $0x4,0x88(%rsp)
    3487:	04 
    3488:	74 1e                	je     34a8 <__progname@@GLIBC_2.2.5-0x5bd8>
    348a:	48 8d 45 02          	lea    0x2(%rbp),%rax
    348e:	4c 39 d8             	cmp    %r11,%rax
    3491:	73 15                	jae    34a8 <__progname@@GLIBC_2.2.5-0x5bd8>
    3493:	48 8b 5c 24 10       	mov    0x10(%rsp),%rbx
    3498:	80 7c 2b 01 3f       	cmpb   $0x3f,0x1(%rbx,%rbp,1)
    349d:	0f 84 dd 06 00 00    	je     3b80 <__progname@@GLIBC_2.2.5-0x5500>
    34a3:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    34a8:	31 d2                	xor    %edx,%edx
    34aa:	45 31 ed             	xor    %r13d,%r13d
    34ad:	bb 3f 00 00 00       	mov    $0x3f,%ebx
    34b2:	e9 01 f9 ff ff       	jmpq   2db8 <__progname@@GLIBC_2.2.5-0x62c8>
    34b7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    34be:	00 00 
    34c0:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    34c5:	0f 85 65 08 00 00    	jne    3d30 <__progname@@GLIBC_2.2.5-0x5350>
    34cb:	45 31 ed             	xor    %r13d,%r13d
    34ce:	31 c0                	xor    %eax,%eax
    34d0:	bb 3f 00 00 00       	mov    $0x3f,%ebx
    34d5:	e9 e6 f9 ff ff       	jmpq   2ec0 <__progname@@GLIBC_2.2.5-0x61c0>
    34da:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    34e0:	48 8d 84 24 b0 00 00 	lea    0xb0(%rsp),%rax
    34e7:	00 
    34e8:	48 c7 84 24 b0 00 00 	movq   $0x0,0xb0(%rsp)
    34ef:	00 00 00 00 00 
    34f4:	48 89 44 24 70       	mov    %rax,0x70(%rsp)
    34f9:	49 83 fb ff          	cmp    $0xffffffffffffffff,%r11
    34fd:	75 2d                	jne    352c <__progname@@GLIBC_2.2.5-0x5b54>
    34ff:	44 89 54 24 38       	mov    %r10d,0x38(%rsp)
    3504:	48 8b 7c 24 10       	mov    0x10(%rsp),%rdi
    3509:	44 88 44 24 30       	mov    %r8b,0x30(%rsp)
    350e:	4c 89 4c 24 28       	mov    %r9,0x28(%rsp)
    3513:	ff 15 cf 59 00 00    	callq  *0x59cf(%rip)        # 8ee8 <strlen@GLIBC_2.2.5>
    3519:	44 8b 54 24 38       	mov    0x38(%rsp),%r10d
    351e:	44 0f b6 44 24 30    	movzbl 0x30(%rsp),%r8d
    3524:	4c 8b 4c 24 28       	mov    0x28(%rsp),%r9
    3529:	49 89 c3             	mov    %rax,%r11
    352c:	31 f6                	xor    %esi,%esi
    352e:	48 8d 84 24 ac 00 00 	lea    0xac(%rsp),%rax
    3535:	00 
    3536:	88 9c 24 8f 00 00 00 	mov    %bl,0x8f(%rsp)
    353d:	4c 89 74 24 78       	mov    %r14,0x78(%rsp)
    3542:	48 89 f3             	mov    %rsi,%rbx
    3545:	4c 8b 74 24 70       	mov    0x70(%rsp),%r14
    354a:	48 89 44 24 38       	mov    %rax,0x38(%rsp)
    354f:	4c 89 8c 24 98 00 00 	mov    %r9,0x98(%rsp)
    3556:	00 
    3557:	44 88 84 24 8e 00 00 	mov    %r8b,0x8e(%rsp)
    355e:	00 
    355f:	48 89 6c 24 30       	mov    %rbp,0x30(%rsp)
    3564:	4c 89 bc 24 90 00 00 	mov    %r15,0x90(%rsp)
    356b:	00 
    356c:	4c 89 a4 24 80 00 00 	mov    %r12,0x80(%rsp)
    3573:	00 
    3574:	4c 89 5c 24 28       	mov    %r11,0x28(%rsp)
    3579:	44 89 54 24 44       	mov    %r10d,0x44(%rsp)
    357e:	eb 2c                	jmp    35ac <__progname@@GLIBC_2.2.5-0x5ad4>
    3580:	8b bc 24 ac 00 00 00 	mov    0xac(%rsp),%edi
    3587:	ff 15 43 5a 00 00    	callq  *0x5a43(%rip)        # 8fd0 <iswprint@GLIBC_2.2.5>
    358d:	4c 89 f7             	mov    %r14,%rdi
    3590:	85 c0                	test   %eax,%eax
    3592:	b8 00 00 00 00       	mov    $0x0,%eax
    3597:	44 0f 44 e8          	cmove  %eax,%r13d
    359b:	48 01 eb             	add    %rbp,%rbx
    359e:	ff 15 24 5a 00 00    	callq  *0x5a24(%rip)        # 8fc8 <mbsinit@GLIBC_2.2.5>
    35a4:	85 c0                	test   %eax,%eax
    35a6:	0f 85 55 05 00 00    	jne    3b01 <__progname@@GLIBC_2.2.5-0x557f>
    35ac:	48 8b 44 24 30       	mov    0x30(%rsp),%rax
    35b1:	48 8b 54 24 28       	mov    0x28(%rsp),%rdx
    35b6:	4c 89 f1             	mov    %r14,%rcx
    35b9:	48 8b 7c 24 38       	mov    0x38(%rsp),%rdi
    35be:	4c 8d 3c 18          	lea    (%rax,%rbx,1),%r15
    35c2:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    35c7:	4c 29 fa             	sub    %r15,%rdx
    35ca:	4e 8d 24 38          	lea    (%rax,%r15,1),%r12
    35ce:	4c 89 e6             	mov    %r12,%rsi
    35d1:	67 e8 69 1b 00 00    	addr32 callq 5140 <__progname@@GLIBC_2.2.5-0x3f40>
    35d7:	48 89 c5             	mov    %rax,%rbp
    35da:	48 85 c0             	test   %rax,%rax
    35dd:	0f 84 1e 05 00 00    	je     3b01 <__progname@@GLIBC_2.2.5-0x557f>
    35e3:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
    35e7:	0f 84 07 06 00 00    	je     3bf4 <__progname@@GLIBC_2.2.5-0x548c>
    35ed:	48 83 f8 fe          	cmp    $0xfffffffffffffffe,%rax
    35f1:	0f 84 42 06 00 00    	je     3c39 <__progname@@GLIBC_2.2.5-0x5447>
    35f7:	83 7c 24 44 02       	cmpl   $0x2,0x44(%rsp)
    35fc:	75 82                	jne    3580 <__progname@@GLIBC_2.2.5-0x5b00>
    35fe:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    3603:	0f 84 77 ff ff ff    	je     3580 <__progname@@GLIBC_2.2.5-0x5b00>
    3609:	48 83 f8 01          	cmp    $0x1,%rax
    360d:	0f 84 6d ff ff ff    	je     3580 <__progname@@GLIBC_2.2.5-0x5b00>
    3613:	48 8b 74 24 10       	mov    0x10(%rsp),%rsi
    3618:	4a 8d 44 3e 01       	lea    0x1(%rsi,%r15,1),%rax
    361d:	48 01 ee             	add    %rbp,%rsi
    3620:	4c 01 fe             	add    %r15,%rsi
    3623:	eb 10                	jmp    3635 <__progname@@GLIBC_2.2.5-0x5a4b>
    3625:	0f 1f 00             	nopl   (%rax)
    3628:	48 83 c0 01          	add    $0x1,%rax
    362c:	48 39 c6             	cmp    %rax,%rsi
    362f:	0f 84 4b ff ff ff    	je     3580 <__progname@@GLIBC_2.2.5-0x5b00>
    3635:	0f b6 38             	movzbl (%rax),%edi
    3638:	8d 4f a5             	lea    -0x5b(%rdi),%ecx
    363b:	80 f9 21             	cmp    $0x21,%cl
    363e:	77 e8                	ja     3628 <__progname@@GLIBC_2.2.5-0x5a58>
    3640:	ba 01 00 00 00       	mov    $0x1,%edx
    3645:	48 d3 e2             	shl    %cl,%rdx
    3648:	48 b9 2b 00 00 00 02 	movabs $0x20000002b,%rcx
    364f:	00 00 00 
    3652:	48 85 ca             	test   %rcx,%rdx
    3655:	74 d1                	je     3628 <__progname@@GLIBC_2.2.5-0x5a58>
    3657:	4c 8b 74 24 78       	mov    0x78(%rsp),%r14
    365c:	4c 8b a4 24 80 00 00 	mov    0x80(%rsp),%r12
    3663:	00 
    3664:	41 bb 02 00 00 00    	mov    $0x2,%r11d
    366a:	48 8b 6c 24 28       	mov    0x28(%rsp),%rbp
    366f:	e9 60 f9 ff ff       	jmpq   2fd4 <__progname@@GLIBC_2.2.5-0x60ac>
    3674:	0f 1f 40 00          	nopl   0x0(%rax)
    3678:	88 44 24 0c          	mov    %al,0xc(%rsp)
    367c:	45 31 ed             	xor    %r13d,%r13d
    367f:	e9 4b f7 ff ff       	jmpq   2dcf <__progname@@GLIBC_2.2.5-0x62b1>
    3684:	0f 1f 40 00          	nopl   0x0(%rax)
    3688:	4c 89 f9             	mov    %r15,%rcx
    368b:	4d 39 fc             	cmp    %r15,%r12
    368e:	0f 86 7e fa ff ff    	jbe    3112 <__progname@@GLIBC_2.2.5-0x5f6e>
    3694:	44 89 c0             	mov    %r8d,%eax
    3697:	e9 6e fa ff ff       	jmpq   310a <__progname@@GLIBC_2.2.5-0x5f76>
    369c:	4d 39 fc             	cmp    %r15,%r12
    369f:	76 05                	jbe    36a6 <__progname@@GLIBC_2.2.5-0x59da>
    36a1:	43 c6 04 3e 27       	movb   $0x27,(%r14,%r15,1)
    36a6:	49 8d 47 01          	lea    0x1(%r15),%rax
    36aa:	49 39 c4             	cmp    %rax,%r12
    36ad:	76 06                	jbe    36b5 <__progname@@GLIBC_2.2.5-0x59cb>
    36af:	43 c6 44 3e 01 5c    	movb   $0x5c,0x1(%r14,%r15,1)
    36b5:	49 8d 47 02          	lea    0x2(%r15),%rax
    36b9:	49 39 c4             	cmp    %rax,%r12
    36bc:	0f 86 9f 07 00 00    	jbe    3e61 <__progname@@GLIBC_2.2.5-0x521f>
    36c2:	4c 89 e2             	mov    %r12,%rdx
    36c5:	43 c6 44 3e 02 27    	movb   $0x27,0x2(%r14,%r15,1)
    36cb:	4c 8b 64 24 50       	mov    0x50(%rsp),%r12
    36d0:	e9 cd f7 ff ff       	jmpq   2ea2 <__progname@@GLIBC_2.2.5-0x61de>
    36d5:	48 83 c5 01          	add    $0x1,%rbp
    36d9:	e9 8a f5 ff ff       	jmpq   2c68 <__progname@@GLIBC_2.2.5-0x6418>
    36de:	0f b6 54 24 08       	movzbl 0x8(%rsp),%edx
    36e3:	45 31 ed             	xor    %r13d,%r13d
    36e6:	48 89 f9             	mov    %rdi,%rcx
    36e9:	44 88 6c 24 28       	mov    %r13b,0x28(%rsp)
    36ee:	31 f6                	xor    %esi,%esi
    36f0:	44 0f b6 6c 24 43    	movzbl 0x43(%rsp),%r13d
    36f6:	48 01 e9             	add    %rbp,%rcx
    36f9:	0f b6 7c 24 0c       	movzbl 0xc(%rsp),%edi
    36fe:	4c 8b 4c 24 10       	mov    0x10(%rsp),%r9
    3703:	e9 b6 00 00 00       	jmpq   37be <__progname@@GLIBC_2.2.5-0x58c2>
    3708:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    370f:	00 
    3710:	41 83 fa 02          	cmp    $0x2,%r10d
    3714:	0f 94 c0             	sete   %al
    3717:	45 84 ed             	test   %r13b,%r13b
    371a:	0f 85 01 01 00 00    	jne    3821 <__progname@@GLIBC_2.2.5-0x585f>
    3720:	44 89 c6             	mov    %r8d,%esi
    3723:	83 f6 01             	xor    $0x1,%esi
    3726:	40 20 f0             	and    %sil,%al
    3729:	74 2f                	je     375a <__progname@@GLIBC_2.2.5-0x5926>
    372b:	4d 39 fc             	cmp    %r15,%r12
    372e:	76 05                	jbe    3735 <__progname@@GLIBC_2.2.5-0x594b>
    3730:	43 c6 04 3e 27       	movb   $0x27,(%r14,%r15,1)
    3735:	49 8d 77 01          	lea    0x1(%r15),%rsi
    3739:	49 39 f4             	cmp    %rsi,%r12
    373c:	76 06                	jbe    3744 <__progname@@GLIBC_2.2.5-0x593c>
    373e:	43 c6 44 3e 01 24    	movb   $0x24,0x1(%r14,%r15,1)
    3744:	49 8d 77 02          	lea    0x2(%r15),%rsi
    3748:	49 39 f4             	cmp    %rsi,%r12
    374b:	76 06                	jbe    3753 <__progname@@GLIBC_2.2.5-0x592d>
    374d:	43 c6 44 3e 02 27    	movb   $0x27,0x2(%r14,%r15,1)
    3753:	49 83 c7 03          	add    $0x3,%r15
    3757:	41 89 c0             	mov    %eax,%r8d
    375a:	4d 39 fc             	cmp    %r15,%r12
    375d:	76 05                	jbe    3764 <__progname@@GLIBC_2.2.5-0x591c>
    375f:	43 c6 04 3e 5c       	movb   $0x5c,(%r14,%r15,1)
    3764:	49 8d 47 01          	lea    0x1(%r15),%rax
    3768:	49 39 c4             	cmp    %rax,%r12
    376b:	76 0d                	jbe    377a <__progname@@GLIBC_2.2.5-0x5906>
    376d:	89 d8                	mov    %ebx,%eax
    376f:	c0 e8 06             	shr    $0x6,%al
    3772:	83 c0 30             	add    $0x30,%eax
    3775:	43 88 44 3e 01       	mov    %al,0x1(%r14,%r15,1)
    377a:	49 8d 47 02          	lea    0x2(%r15),%rax
    377e:	49 39 c4             	cmp    %rax,%r12
    3781:	76 10                	jbe    3793 <__progname@@GLIBC_2.2.5-0x58ed>
    3783:	89 d8                	mov    %ebx,%eax
    3785:	c0 e8 03             	shr    $0x3,%al
    3788:	83 e0 07             	and    $0x7,%eax
    378b:	83 c0 30             	add    $0x30,%eax
    378e:	43 88 44 3e 02       	mov    %al,0x2(%r14,%r15,1)
    3793:	83 e3 07             	and    $0x7,%ebx
    3796:	48 83 c5 01          	add    $0x1,%rbp
    379a:	49 83 c7 03          	add    $0x3,%r15
    379e:	83 c3 30             	add    $0x30,%ebx
    37a1:	48 39 cd             	cmp    %rcx,%rbp
    37a4:	0f 83 36 03 00 00    	jae    3ae0 <__progname@@GLIBC_2.2.5-0x55a0>
    37aa:	89 d6                	mov    %edx,%esi
    37ac:	4d 39 fc             	cmp    %r15,%r12
    37af:	76 04                	jbe    37b5 <__progname@@GLIBC_2.2.5-0x58cb>
    37b1:	43 88 1c 3e          	mov    %bl,(%r14,%r15,1)
    37b5:	41 0f b6 1c 29       	movzbl (%r9,%rbp,1),%ebx
    37ba:	49 83 c7 01          	add    $0x1,%r15
    37be:	84 d2                	test   %dl,%dl
    37c0:	0f 85 4a ff ff ff    	jne    3710 <__progname@@GLIBC_2.2.5-0x5970>
    37c6:	89 f0                	mov    %esi,%eax
    37c8:	83 f0 01             	xor    $0x1,%eax
    37cb:	44 21 c0             	and    %r8d,%eax
    37ce:	40 84 ff             	test   %dil,%dil
    37d1:	74 0e                	je     37e1 <__progname@@GLIBC_2.2.5-0x589f>
    37d3:	4d 39 fc             	cmp    %r15,%r12
    37d6:	76 05                	jbe    37dd <__progname@@GLIBC_2.2.5-0x58a3>
    37d8:	43 c6 04 3e 5c       	movb   $0x5c,(%r14,%r15,1)
    37dd:	49 83 c7 01          	add    $0x1,%r15
    37e1:	48 83 c5 01          	add    $0x1,%rbp
    37e5:	48 39 cd             	cmp    %rcx,%rbp
    37e8:	73 2c                	jae    3816 <__progname@@GLIBC_2.2.5-0x586a>
    37ea:	84 c0                	test   %al,%al
    37ec:	0f 84 08 03 00 00    	je     3afa <__progname@@GLIBC_2.2.5-0x5586>
    37f2:	4d 39 fc             	cmp    %r15,%r12
    37f5:	76 05                	jbe    37fc <__progname@@GLIBC_2.2.5-0x5884>
    37f7:	43 c6 04 3e 27       	movb   $0x27,(%r14,%r15,1)
    37fc:	49 8d 47 01          	lea    0x1(%r15),%rax
    3800:	49 39 c4             	cmp    %rax,%r12
    3803:	76 06                	jbe    380b <__progname@@GLIBC_2.2.5-0x5875>
    3805:	43 c6 44 3e 01 27    	movb   $0x27,0x1(%r14,%r15,1)
    380b:	49 83 c7 02          	add    $0x2,%r15
    380f:	31 ff                	xor    %edi,%edi
    3811:	45 31 c0             	xor    %r8d,%r8d
    3814:	eb 96                	jmp    37ac <__progname@@GLIBC_2.2.5-0x58d4>
    3816:	44 0f b6 6c 24 28    	movzbl 0x28(%rsp),%r13d
    381c:	e9 bb f6 ff ff       	jmpq   2edc <__progname@@GLIBC_2.2.5-0x61a4>
    3821:	4c 89 dd             	mov    %r11,%rbp
    3824:	88 44 24 08          	mov    %al,0x8(%rsp)
    3828:	45 89 d3             	mov    %r10d,%r11d
    382b:	e9 a4 f7 ff ff       	jmpq   2fd4 <__progname@@GLIBC_2.2.5-0x60ac>
    3830:	49 83 c7 04          	add    $0x4,%r15
    3834:	41 89 c0             	mov    %eax,%r8d
    3837:	45 31 ed             	xor    %r13d,%r13d
    383a:	bb 30 00 00 00       	mov    $0x30,%ebx
    383f:	e9 7c f6 ff ff       	jmpq   2ec0 <__progname@@GLIBC_2.2.5-0x61c0>
    3844:	85 db                	test   %ebx,%ebx
    3846:	0f 85 c2 f3 ff ff    	jne    2c0e <__progname@@GLIBC_2.2.5-0x6472>
    384c:	c6 44 24 08 01       	movb   $0x1,0x8(%rsp)
    3851:	4d 85 e4             	test   %r12,%r12
    3854:	0f 85 e5 05 00 00    	jne    3e3f <__progname@@GLIBC_2.2.5-0x5241>
    385a:	48 8d 05 dc 2a 00 00 	lea    0x2adc(%rip),%rax        # 633d <__progname@@GLIBC_2.2.5-0x2d43>
    3861:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3866:	45 31 ed             	xor    %r13d,%r13d
    3869:	41 bf 01 00 00 00    	mov    $0x1,%r15d
    386f:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3876:	00 00 
    3878:	41 bb 02 00 00 00    	mov    $0x2,%r11d
    387e:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    3885:	00 
    3886:	c6 44 24 43 00       	movb   $0x0,0x43(%rsp)
    388b:	48 c7 44 24 18 01 00 	movq   $0x1,0x18(%rsp)
    3892:	00 00 
    3894:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    3899:	e9 b1 f3 ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    389e:	85 db                	test   %ebx,%ebx
    38a0:	0f 85 4a 04 00 00    	jne    3cf0 <__progname@@GLIBC_2.2.5-0x5390>
    38a6:	4d 85 e4             	test   %r12,%r12
    38a9:	0f 84 a3 02 00 00    	je     3b52 <__progname@@GLIBC_2.2.5-0x552e>
    38af:	41 c6 06 22          	movb   $0x22,(%r14)
    38b3:	45 31 ed             	xor    %r13d,%r13d
    38b6:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    38bb:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    38c2:	00 
    38c3:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    38ca:	00 00 
    38cc:	48 8d 05 59 2a 00 00 	lea    0x2a59(%rip),%rax        # 632c <__progname@@GLIBC_2.2.5-0x2d54>
    38d3:	c6 44 24 43 00       	movb   $0x0,0x43(%rsp)
    38d8:	41 bf 01 00 00 00    	mov    $0x1,%r15d
    38de:	c6 44 24 08 01       	movb   $0x1,0x8(%rsp)
    38e3:	48 c7 44 24 18 01 00 	movq   $0x1,0x18(%rsp)
    38ea:	00 00 
    38ec:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    38f1:	e9 59 f3 ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    38f6:	41 83 fb 0a          	cmp    $0xa,%r11d
    38fa:	74 37                	je     3933 <__progname@@GLIBC_2.2.5-0x574d>
    38fc:	44 89 de             	mov    %r11d,%esi
    38ff:	48 8d 3d 39 2a 00 00 	lea    0x2a39(%rip),%rdi        # 633f <__progname@@GLIBC_2.2.5-0x2d41>
    3906:	44 89 5c 24 08       	mov    %r11d,0x8(%rsp)
    390b:	e8 50 f1 ff ff       	callq  2a60 <__progname@@GLIBC_2.2.5-0x6620>
    3910:	44 8b 5c 24 08       	mov    0x8(%rsp),%r11d
    3915:	48 8d 3d 21 2a 00 00 	lea    0x2a21(%rip),%rdi        # 633d <__progname@@GLIBC_2.2.5-0x2d43>
    391c:	48 89 44 24 68       	mov    %rax,0x68(%rsp)
    3921:	44 89 de             	mov    %r11d,%esi
    3924:	e8 37 f1 ff ff       	callq  2a60 <__progname@@GLIBC_2.2.5-0x6620>
    3929:	44 8b 5c 24 08       	mov    0x8(%rsp),%r11d
    392e:	48 89 44 24 60       	mov    %rax,0x60(%rsp)
    3933:	45 31 ff             	xor    %r15d,%r15d
    3936:	85 db                	test   %ebx,%ebx
    3938:	0f 84 77 03 00 00    	je     3cb5 <__progname@@GLIBC_2.2.5-0x53cb>
    393e:	48 8b 5c 24 60       	mov    0x60(%rsp),%rbx
    3943:	44 89 5c 24 0c       	mov    %r11d,0xc(%rsp)
    3948:	45 31 ed             	xor    %r13d,%r13d
    394b:	48 89 df             	mov    %rbx,%rdi
    394e:	ff 15 94 55 00 00    	callq  *0x5594(%rip)        # 8ee8 <strlen@GLIBC_2.2.5>
    3954:	48 89 5c 24 48       	mov    %rbx,0x48(%rsp)
    3959:	44 8b 5c 24 0c       	mov    0xc(%rsp),%r11d
    395e:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    3963:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3968:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    396f:	00 
    3970:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3977:	00 00 
    3979:	c6 44 24 08 01       	movb   $0x1,0x8(%rsp)
    397e:	e9 cc f2 ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    3983:	48 8d 05 a2 29 00 00 	lea    0x29a2(%rip),%rax        # 632c <__progname@@GLIBC_2.2.5-0x2d54>
    398a:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    398f:	45 31 ed             	xor    %r13d,%r13d
    3992:	45 31 ff             	xor    %r15d,%r15d
    3995:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    399c:	00 
    399d:	41 bb 05 00 00 00    	mov    $0x5,%r11d
    39a3:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    39aa:	00 00 
    39ac:	c6 44 24 43 01       	movb   $0x1,0x43(%rsp)
    39b1:	c6 44 24 08 01       	movb   $0x1,0x8(%rsp)
    39b6:	48 c7 44 24 18 01 00 	movq   $0x1,0x18(%rsp)
    39bd:	00 00 
    39bf:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    39c4:	e9 86 f2 ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    39c9:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    39ce:	45 31 ed             	xor    %r13d,%r13d
    39d1:	45 31 ff             	xor    %r15d,%r15d
    39d4:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    39db:	00 
    39dc:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    39e3:	00 00 
    39e5:	c6 44 24 43 00       	movb   $0x0,0x43(%rsp)
    39ea:	c6 44 24 08 01       	movb   $0x1,0x8(%rsp)
    39ef:	48 c7 44 24 18 00 00 	movq   $0x0,0x18(%rsp)
    39f6:	00 00 
    39f8:	48 c7 44 24 48 00 00 	movq   $0x0,0x48(%rsp)
    39ff:	00 00 
    3a01:	e9 49 f2 ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    3a06:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3a0b:	45 31 ed             	xor    %r13d,%r13d
    3a0e:	45 31 ff             	xor    %r15d,%r15d
    3a11:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    3a18:	00 
    3a19:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3a20:	00 00 
    3a22:	c6 44 24 43 00       	movb   $0x0,0x43(%rsp)
    3a27:	c6 44 24 08 00       	movb   $0x0,0x8(%rsp)
    3a2c:	48 c7 44 24 18 00 00 	movq   $0x0,0x18(%rsp)
    3a33:	00 00 
    3a35:	48 c7 44 24 48 00 00 	movq   $0x0,0x48(%rsp)
    3a3c:	00 00 
    3a3e:	e9 0c f2 ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    3a43:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3a48:	45 31 ed             	xor    %r13d,%r13d
    3a4b:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    3a52:	00 
    3a53:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3a5a:	00 00 
    3a5c:	c6 44 24 43 01       	movb   $0x1,0x43(%rsp)
    3a61:	c6 44 24 08 01       	movb   $0x1,0x8(%rsp)
    3a66:	e9 c6 f1 ff ff       	jmpq   2c31 <__progname@@GLIBC_2.2.5-0x644f>
    3a6b:	0f b6 44 24 0c       	movzbl 0xc(%rsp),%eax
    3a70:	e9 45 f9 ff ff       	jmpq   33ba <__progname@@GLIBC_2.2.5-0x5cc6>
    3a75:	31 d2                	xor    %edx,%edx
    3a77:	45 31 ed             	xor    %r13d,%r13d
    3a7a:	bb 62 00 00 00       	mov    $0x62,%ebx
    3a7f:	e9 85 f3 ff ff       	jmpq   2e09 <__progname@@GLIBC_2.2.5-0x6277>
    3a84:	bb 61 00 00 00       	mov    $0x61,%ebx
    3a89:	e9 0a f6 ff ff       	jmpq   3098 <__progname@@GLIBC_2.2.5-0x5fe8>
    3a8e:	0f b6 44 24 0c       	movzbl 0xc(%rsp),%eax
    3a93:	e9 ea f8 ff ff       	jmpq   3382 <__progname@@GLIBC_2.2.5-0x5cfe>
    3a98:	0f b6 44 24 0c       	movzbl 0xc(%rsp),%eax
    3a9d:	e9 f8 f8 ff ff       	jmpq   339a <__progname@@GLIBC_2.2.5-0x5ce6>
    3aa2:	4d 39 fc             	cmp    %r15,%r12
    3aa5:	76 05                	jbe    3aac <__progname@@GLIBC_2.2.5-0x55d4>
    3aa7:	43 c6 04 3e 30       	movb   $0x30,(%r14,%r15,1)
    3aac:	48 8d 41 02          	lea    0x2(%rcx),%rax
    3ab0:	49 39 c4             	cmp    %rax,%r12
    3ab3:	76 06                	jbe    3abb <__progname@@GLIBC_2.2.5-0x55c5>
    3ab5:	41 c6 44 0e 02 30    	movb   $0x30,0x2(%r14,%rcx,1)
    3abb:	4c 8d 79 03          	lea    0x3(%rcx),%r15
    3abf:	bb 30 00 00 00       	mov    $0x30,%ebx
    3ac4:	e9 7e f6 ff ff       	jmpq   3147 <__progname@@GLIBC_2.2.5-0x5f39>
    3ac9:	85 db                	test   %ebx,%ebx
    3acb:	0f 85 2e 03 00 00    	jne    3dff <__progname@@GLIBC_2.2.5-0x5281>
    3ad1:	c6 44 24 08 00       	movb   $0x0,0x8(%rsp)
    3ad6:	e9 76 fd ff ff       	jmpq   3851 <__progname@@GLIBC_2.2.5-0x582f>
    3adb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    3ae0:	44 0f b6 6c 24 28    	movzbl 0x28(%rsp),%r13d
    3ae6:	e9 69 f3 ff ff       	jmpq   2e54 <__progname@@GLIBC_2.2.5-0x622c>
    3aeb:	48 83 c5 01          	add    $0x1,%rbp
    3aef:	44 89 c0             	mov    %r8d,%eax
    3af2:	45 31 ed             	xor    %r13d,%r13d
    3af5:	e9 e2 f3 ff ff       	jmpq   2edc <__progname@@GLIBC_2.2.5-0x61a4>
    3afa:	31 ff                	xor    %edi,%edi
    3afc:	e9 ab fc ff ff       	jmpq   37ac <__progname@@GLIBC_2.2.5-0x58d4>
    3b01:	48 89 df             	mov    %rbx,%rdi
    3b04:	44 89 ea             	mov    %r13d,%edx
    3b07:	48 8b 6c 24 30       	mov    0x30(%rsp),%rbp
    3b0c:	4c 8b 74 24 78       	mov    0x78(%rsp),%r14
    3b11:	0f b6 9c 24 8f 00 00 	movzbl 0x8f(%rsp),%ebx
    3b18:	00 
    3b19:	4c 8b 5c 24 28       	mov    0x28(%rsp),%r11
    3b1e:	83 f2 01             	xor    $0x1,%edx
    3b21:	44 0f b6 84 24 8e 00 	movzbl 0x8e(%rsp),%r8d
    3b28:	00 00 
    3b2a:	4c 8b bc 24 90 00 00 	mov    0x90(%rsp),%r15
    3b31:	00 
    3b32:	4c 8b a4 24 80 00 00 	mov    0x80(%rsp),%r12
    3b39:	00 
    3b3a:	44 8b 54 24 44       	mov    0x44(%rsp),%r10d
    3b3f:	22 54 24 08          	and    0x8(%rsp),%dl
    3b43:	48 83 ff 01          	cmp    $0x1,%rdi
    3b47:	0f 87 99 fb ff ff    	ja     36e6 <__progname@@GLIBC_2.2.5-0x599a>
    3b4d:	e9 6a f6 ff ff       	jmpq   31bc <__progname@@GLIBC_2.2.5-0x5ec4>
    3b52:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3b59:	00 00 
    3b5b:	45 31 ed             	xor    %r13d,%r13d
    3b5e:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3b63:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    3b6a:	00 
    3b6b:	e9 5c fd ff ff       	jmpq   38cc <__progname@@GLIBC_2.2.5-0x57b4>
    3b70:	44 89 e8             	mov    %r13d,%eax
    3b73:	bb 30 00 00 00       	mov    $0x30,%ebx
    3b78:	45 31 ed             	xor    %r13d,%r13d
    3b7b:	e9 40 f3 ff ff       	jmpq   2ec0 <__progname@@GLIBC_2.2.5-0x61c0>
    3b80:	0f b6 1c 03          	movzbl (%rbx,%rax,1),%ebx
    3b84:	80 fb 3e             	cmp    $0x3e,%bl
    3b87:	0f 87 1b f9 ff ff    	ja     34a8 <__progname@@GLIBC_2.2.5-0x5bd8>
    3b8d:	48 be 00 00 00 00 82 	movabs $0x7000a38200000000,%rsi
    3b94:	a3 00 70 
    3b97:	48 0f a3 de          	bt     %rbx,%rsi
    3b9b:	0f 83 07 f9 ff ff    	jae    34a8 <__progname@@GLIBC_2.2.5-0x5bd8>
    3ba1:	80 7c 24 43 00       	cmpb   $0x0,0x43(%rsp)
    3ba6:	0f 85 8f 01 00 00    	jne    3d3b <__progname@@GLIBC_2.2.5-0x5345>
    3bac:	4d 39 fc             	cmp    %r15,%r12
    3baf:	76 05                	jbe    3bb6 <__progname@@GLIBC_2.2.5-0x54ca>
    3bb1:	43 c6 04 3e 3f       	movb   $0x3f,(%r14,%r15,1)
    3bb6:	49 8d 57 01          	lea    0x1(%r15),%rdx
    3bba:	49 39 d4             	cmp    %rdx,%r12
    3bbd:	76 06                	jbe    3bc5 <__progname@@GLIBC_2.2.5-0x54bb>
    3bbf:	43 c6 44 3e 01 22    	movb   $0x22,0x1(%r14,%r15,1)
    3bc5:	49 8d 57 02          	lea    0x2(%r15),%rdx
    3bc9:	49 39 d4             	cmp    %rdx,%r12
    3bcc:	76 06                	jbe    3bd4 <__progname@@GLIBC_2.2.5-0x54ac>
    3bce:	43 c6 44 3e 02 22    	movb   $0x22,0x2(%r14,%r15,1)
    3bd4:	49 8d 57 03          	lea    0x3(%r15),%rdx
    3bd8:	49 39 d4             	cmp    %rdx,%r12
    3bdb:	76 06                	jbe    3be3 <__progname@@GLIBC_2.2.5-0x549d>
    3bdd:	43 c6 44 3e 03 3f    	movb   $0x3f,0x3(%r14,%r15,1)
    3be3:	49 83 c7 04          	add    $0x4,%r15
    3be7:	31 d2                	xor    %edx,%edx
    3be9:	45 31 ed             	xor    %r13d,%r13d
    3bec:	48 89 c5             	mov    %rax,%rbp
    3bef:	e9 53 f5 ff ff       	jmpq   3147 <__progname@@GLIBC_2.2.5-0x5f39>
    3bf4:	48 89 df             	mov    %rbx,%rdi
    3bf7:	48 8b 6c 24 30       	mov    0x30(%rsp),%rbp
    3bfc:	4c 8b 74 24 78       	mov    0x78(%rsp),%r14
    3c01:	45 31 ed             	xor    %r13d,%r13d
    3c04:	44 0f b6 84 24 8e 00 	movzbl 0x8e(%rsp),%r8d
    3c0b:	00 00 
    3c0d:	0f b6 9c 24 8f 00 00 	movzbl 0x8f(%rsp),%ebx
    3c14:	00 
    3c15:	4c 8b bc 24 90 00 00 	mov    0x90(%rsp),%r15
    3c1c:	00 
    3c1d:	4c 8b a4 24 80 00 00 	mov    0x80(%rsp),%r12
    3c24:	00 
    3c25:	4c 8b 5c 24 28       	mov    0x28(%rsp),%r11
    3c2a:	44 8b 54 24 44       	mov    0x44(%rsp),%r10d
    3c2f:	0f b6 54 24 08       	movzbl 0x8(%rsp),%edx
    3c34:	e9 0a ff ff ff       	jmpq   3b43 <__progname@@GLIBC_2.2.5-0x553d>
    3c39:	4c 8b 5c 24 28       	mov    0x28(%rsp),%r11
    3c3e:	4c 89 fe             	mov    %r15,%rsi
    3c41:	4c 89 e1             	mov    %r12,%rcx
    3c44:	48 89 d8             	mov    %rbx,%rax
    3c47:	48 89 df             	mov    %rbx,%rdi
    3c4a:	48 8b 6c 24 30       	mov    0x30(%rsp),%rbp
    3c4f:	4c 8b 74 24 78       	mov    0x78(%rsp),%r14
    3c54:	4c 8b 8c 24 98 00 00 	mov    0x98(%rsp),%r9
    3c5b:	00 
    3c5c:	0f b6 9c 24 8f 00 00 	movzbl 0x8f(%rsp),%ebx
    3c63:	00 
    3c64:	44 0f b6 84 24 8e 00 	movzbl 0x8e(%rsp),%r8d
    3c6b:	00 00 
    3c6d:	4c 8b bc 24 90 00 00 	mov    0x90(%rsp),%r15
    3c74:	00 
    3c75:	4c 8b a4 24 80 00 00 	mov    0x80(%rsp),%r12
    3c7c:	00 
    3c7d:	44 8b 54 24 44       	mov    0x44(%rsp),%r10d
    3c82:	4c 39 de             	cmp    %r11,%rsi
    3c85:	73 21                	jae    3ca8 <__progname@@GLIBC_2.2.5-0x53d8>
    3c87:	80 39 00             	cmpb   $0x0,(%rcx)
    3c8a:	75 0b                	jne    3c97 <__progname@@GLIBC_2.2.5-0x53e9>
    3c8c:	eb 1a                	jmp    3ca8 <__progname@@GLIBC_2.2.5-0x53d8>
    3c8e:	66 90                	xchg   %ax,%ax
    3c90:	41 80 3c 01 00       	cmpb   $0x0,(%r9,%rax,1)
    3c95:	74 0e                	je     3ca5 <__progname@@GLIBC_2.2.5-0x53db>
    3c97:	48 83 c0 01          	add    $0x1,%rax
    3c9b:	48 8d 54 05 00       	lea    0x0(%rbp,%rax,1),%rdx
    3ca0:	4c 39 da             	cmp    %r11,%rdx
    3ca3:	72 eb                	jb     3c90 <__progname@@GLIBC_2.2.5-0x53f0>
    3ca5:	48 89 c7             	mov    %rax,%rdi
    3ca8:	0f b6 54 24 08       	movzbl 0x8(%rsp),%edx
    3cad:	45 31 ed             	xor    %r13d,%r13d
    3cb0:	e9 8e fe ff ff       	jmpq   3b43 <__progname@@GLIBC_2.2.5-0x553d>
    3cb5:	48 8b 54 24 68       	mov    0x68(%rsp),%rdx
    3cba:	0f b6 02             	movzbl (%rdx),%eax
    3cbd:	84 c0                	test   %al,%al
    3cbf:	0f 84 79 fc ff ff    	je     393e <__progname@@GLIBC_2.2.5-0x5742>
    3cc5:	0f 1f 00             	nopl   (%rax)
    3cc8:	4d 39 fc             	cmp    %r15,%r12
    3ccb:	76 04                	jbe    3cd1 <__progname@@GLIBC_2.2.5-0x53af>
    3ccd:	43 88 04 3e          	mov    %al,(%r14,%r15,1)
    3cd1:	49 83 c7 01          	add    $0x1,%r15
    3cd5:	42 0f b6 04 3a       	movzbl (%rdx,%r15,1),%eax
    3cda:	84 c0                	test   %al,%al
    3cdc:	75 ea                	jne    3cc8 <__progname@@GLIBC_2.2.5-0x53b8>
    3cde:	e9 5b fc ff ff       	jmpq   393e <__progname@@GLIBC_2.2.5-0x5742>
    3ce3:	4c 89 dd             	mov    %r11,%rbp
    3ce6:	31 c0                	xor    %eax,%eax
    3ce8:	45 89 d3             	mov    %r10d,%r11d
    3ceb:	e9 e0 f2 ff ff       	jmpq   2fd0 <__progname@@GLIBC_2.2.5-0x60b0>
    3cf0:	48 8d 05 35 26 00 00 	lea    0x2635(%rip),%rax        # 632c <__progname@@GLIBC_2.2.5-0x2d54>
    3cf7:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3cfc:	45 31 ed             	xor    %r13d,%r13d
    3cff:	45 31 ff             	xor    %r15d,%r15d
    3d02:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    3d09:	00 
    3d0a:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3d11:	00 00 
    3d13:	c6 44 24 43 01       	movb   $0x1,0x43(%rsp)
    3d18:	c6 44 24 08 01       	movb   $0x1,0x8(%rsp)
    3d1d:	48 c7 44 24 18 01 00 	movq   $0x1,0x18(%rsp)
    3d24:	00 00 
    3d26:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    3d2b:	e9 1f ef ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    3d30:	4c 89 dd             	mov    %r11,%rbp
    3d33:	45 89 d3             	mov    %r10d,%r11d
    3d36:	e9 99 f2 ff ff       	jmpq   2fd4 <__progname@@GLIBC_2.2.5-0x60ac>
    3d3b:	4c 89 dd             	mov    %r11,%rbp
    3d3e:	45 89 d3             	mov    %r10d,%r11d
    3d41:	e9 9c f2 ff ff       	jmpq   2fe2 <__progname@@GLIBC_2.2.5-0x609e>
    3d46:	89 c2                	mov    %eax,%edx
    3d48:	48 8b 44 24 48       	mov    0x48(%rsp),%rax
    3d4d:	48 85 c0             	test   %rax,%rax
    3d50:	74 29                	je     3d7b <__progname@@GLIBC_2.2.5-0x5305>
    3d52:	84 d2                	test   %dl,%dl
    3d54:	74 25                	je     3d7b <__progname@@GLIBC_2.2.5-0x5305>
    3d56:	0f b6 08             	movzbl (%rax),%ecx
    3d59:	84 c9                	test   %cl,%cl
    3d5b:	74 1e                	je     3d7b <__progname@@GLIBC_2.2.5-0x5305>
    3d5d:	4c 89 fa             	mov    %r15,%rdx
    3d60:	4c 29 f8             	sub    %r15,%rax
    3d63:	49 39 d4             	cmp    %rdx,%r12
    3d66:	76 04                	jbe    3d6c <__progname@@GLIBC_2.2.5-0x5314>
    3d68:	41 88 0c 16          	mov    %cl,(%r14,%rdx,1)
    3d6c:	48 83 c2 01          	add    $0x1,%rdx
    3d70:	0f b6 0c 10          	movzbl (%rax,%rdx,1),%ecx
    3d74:	84 c9                	test   %cl,%cl
    3d76:	75 eb                	jne    3d63 <__progname@@GLIBC_2.2.5-0x531d>
    3d78:	49 89 d7             	mov    %rdx,%r15
    3d7b:	4d 39 fc             	cmp    %r15,%r12
    3d7e:	0f 86 95 f2 ff ff    	jbe    3019 <__progname@@GLIBC_2.2.5-0x6067>
    3d84:	43 c6 04 3e 00       	movb   $0x0,(%r14,%r15,1)
    3d89:	e9 8b f2 ff ff       	jmpq   3019 <__progname@@GLIBC_2.2.5-0x6067>
    3d8e:	41 83 fa 02          	cmp    $0x2,%r10d
    3d92:	4c 89 dd             	mov    %r11,%rbp
    3d95:	45 89 d3             	mov    %r10d,%r11d
    3d98:	0f 94 44 24 08       	sete   0x8(%rsp)
    3d9d:	e9 32 f2 ff ff       	jmpq   2fd4 <__progname@@GLIBC_2.2.5-0x60ac>
    3da2:	48 83 ec 08          	sub    $0x8,%rsp
    3da6:	41 b8 05 00 00 00    	mov    $0x5,%r8d
    3dac:	48 89 e9             	mov    %rbp,%rcx
    3daf:	4c 89 f7             	mov    %r14,%rdi
    3db2:	ff 74 24 68          	pushq  0x68(%rsp)
    3db6:	ff 74 24 78          	pushq  0x78(%rsp)
    3dba:	ff 74 24 38          	pushq  0x38(%rsp)
    3dbe:	44 8b 8c 24 a8 00 00 	mov    0xa8(%rsp),%r9d
    3dc5:	00 
    3dc6:	48 8b 54 24 30       	mov    0x30(%rsp),%rdx
    3dcb:	48 8b 74 24 70       	mov    0x70(%rsp),%rsi
    3dd0:	e8 9b ed ff ff       	callq  2b70 <__progname@@GLIBC_2.2.5-0x6510>
    3dd5:	48 83 c4 20          	add    $0x20,%rsp
    3dd9:	49 89 c7             	mov    %rax,%r15
    3ddc:	e9 38 f2 ff ff       	jmpq   3019 <__progname@@GLIBC_2.2.5-0x6067>
    3de1:	0f b6 94 24 8d 00 00 	movzbl 0x8d(%rsp),%edx
    3de8:	00 
    3de9:	e9 5a ff ff ff       	jmpq   3d48 <__progname@@GLIBC_2.2.5-0x5338>
    3dee:	41 bb 02 00 00 00    	mov    $0x2,%r11d
    3df4:	e9 db f1 ff ff       	jmpq   2fd4 <__progname@@GLIBC_2.2.5-0x60ac>
    3df9:	ff 15 f1 50 00 00    	callq  *0x50f1(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    3dff:	48 8d 05 37 25 00 00 	lea    0x2537(%rip),%rax        # 633d <__progname@@GLIBC_2.2.5-0x2d43>
    3e06:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3e0b:	45 31 ed             	xor    %r13d,%r13d
    3e0e:	45 31 ff             	xor    %r15d,%r15d
    3e11:	c6 84 24 8d 00 00 00 	movb   $0x0,0x8d(%rsp)
    3e18:	00 
    3e19:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3e20:	00 00 
    3e22:	c6 44 24 43 01       	movb   $0x1,0x43(%rsp)
    3e27:	c6 44 24 08 00       	movb   $0x0,0x8(%rsp)
    3e2c:	48 c7 44 24 18 01 00 	movq   $0x1,0x18(%rsp)
    3e33:	00 00 
    3e35:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    3e3a:	e9 10 ee ff ff       	jmpq   2c4f <__progname@@GLIBC_2.2.5-0x6431>
    3e3f:	45 31 ed             	xor    %r13d,%r13d
    3e42:	31 c0                	xor    %eax,%eax
    3e44:	c6 44 24 42 01       	movb   $0x1,0x42(%rsp)
    3e49:	48 c7 44 24 50 00 00 	movq   $0x0,0x50(%rsp)
    3e50:	00 00 
    3e52:	e9 f2 f5 ff ff       	jmpq   3449 <__progname@@GLIBC_2.2.5-0x5c37>
    3e57:	89 cb                	mov    %ecx,%ebx
    3e59:	45 31 ed             	xor    %r13d,%r13d
    3e5c:	e9 9d ef ff ff       	jmpq   2dfe <__progname@@GLIBC_2.2.5-0x6282>
    3e61:	4c 89 e2             	mov    %r12,%rdx
    3e64:	4c 8b 64 24 50       	mov    0x50(%rsp),%r12
    3e69:	e9 34 f0 ff ff       	jmpq   2ea2 <__progname@@GLIBC_2.2.5-0x61de>
    3e6e:	66 90                	xchg   %ax,%ax
    3e70:	41 57                	push   %r15
    3e72:	4c 63 ff             	movslq %edi,%r15
    3e75:	41 56                	push   %r14
    3e77:	49 89 d6             	mov    %rdx,%r14
    3e7a:	41 55                	push   %r13
    3e7c:	41 54                	push   %r12
    3e7e:	55                   	push   %rbp
    3e7f:	48 89 cd             	mov    %rcx,%rbp
    3e82:	53                   	push   %rbx
    3e83:	48 83 ec 28          	sub    $0x28,%rsp
    3e87:	48 89 74 24 08       	mov    %rsi,0x8(%rsp)
    3e8c:	ff 15 fe 4f 00 00    	callq  *0x4ffe(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    3e92:	48 8b 1d c7 51 00 00 	mov    0x51c7(%rip),%rbx        # 9060 <__progname@@GLIBC_2.2.5-0x20>
    3e99:	49 89 c5             	mov    %rax,%r13
    3e9c:	8b 00                	mov    (%rax),%eax
    3e9e:	89 44 24 18          	mov    %eax,0x18(%rsp)
    3ea2:	45 85 ff             	test   %r15d,%r15d
    3ea5:	0f 88 7b e1 ff ff    	js     2026 <__progname@@GLIBC_2.2.5-0x705a>
    3eab:	44 39 3d a6 51 00 00 	cmp    %r15d,0x51a6(%rip)        # 9058 <__progname@@GLIBC_2.2.5-0x28>
    3eb2:	7f 64                	jg     3f18 <__progname@@GLIBC_2.2.5-0x5168>
    3eb4:	41 81 ff ff ff ff 7f 	cmp    $0x7fffffff,%r15d
    3ebb:	0f 84 51 01 00 00    	je     4012 <__progname@@GLIBC_2.2.5-0x506e>
    3ec1:	45 8d 67 01          	lea    0x1(%r15),%r12d
    3ec5:	48 8d 05 a4 51 00 00 	lea    0x51a4(%rip),%rax        # 9070 <__progname@@GLIBC_2.2.5-0x10>
    3ecc:	49 63 f4             	movslq %r12d,%rsi
    3ecf:	48 c1 e6 04          	shl    $0x4,%rsi
    3ed3:	48 39 c3             	cmp    %rax,%rbx
    3ed6:	0f 84 14 01 00 00    	je     3ff0 <__progname@@GLIBC_2.2.5-0x5090>
    3edc:	48 89 df             	mov    %rbx,%rdi
    3edf:	67 e8 1b 10 00 00    	addr32 callq 4f00 <__progname@@GLIBC_2.2.5-0x4180>
    3ee5:	48 89 05 74 51 00 00 	mov    %rax,0x5174(%rip)        # 9060 <__progname@@GLIBC_2.2.5-0x20>
    3eec:	48 89 c3             	mov    %rax,%rbx
    3eef:	48 63 3d 62 51 00 00 	movslq 0x5162(%rip),%rdi        # 9058 <__progname@@GLIBC_2.2.5-0x28>
    3ef6:	44 89 e2             	mov    %r12d,%edx
    3ef9:	31 f6                	xor    %esi,%esi
    3efb:	29 fa                	sub    %edi,%edx
    3efd:	48 c1 e7 04          	shl    $0x4,%rdi
    3f01:	48 63 d2             	movslq %edx,%rdx
    3f04:	48 01 df             	add    %rbx,%rdi
    3f07:	48 c1 e2 04          	shl    $0x4,%rdx
    3f0b:	ff 15 07 50 00 00    	callq  *0x5007(%rip)        # 8f18 <memset@GLIBC_2.2.5>
    3f11:	44 89 25 40 51 00 00 	mov    %r12d,0x5140(%rip)        # 9058 <__progname@@GLIBC_2.2.5-0x28>
    3f18:	8b 45 04             	mov    0x4(%rbp),%eax
    3f1b:	49 c1 e7 04          	shl    $0x4,%r15
    3f1f:	48 83 ec 08          	sub    $0x8,%rsp
    3f23:	44 8b 45 00          	mov    0x0(%rbp),%r8d
    3f27:	4c 01 fb             	add    %r15,%rbx
    3f2a:	4c 8d 7d 08          	lea    0x8(%rbp),%r15
    3f2e:	4c 89 f1             	mov    %r14,%rcx
    3f31:	83 c8 01             	or     $0x1,%eax
    3f34:	4c 8b 1b             	mov    (%rbx),%r11
    3f37:	4c 8b 63 08          	mov    0x8(%rbx),%r12
    3f3b:	89 44 24 24          	mov    %eax,0x24(%rsp)
    3f3f:	41 89 c1             	mov    %eax,%r9d
    3f42:	ff 75 30             	pushq  0x30(%rbp)
    3f45:	4c 89 de             	mov    %r11,%rsi
    3f48:	4c 89 e7             	mov    %r12,%rdi
    3f4b:	ff 75 28             	pushq  0x28(%rbp)
    3f4e:	41 57                	push   %r15
    3f50:	48 8b 54 24 28       	mov    0x28(%rsp),%rdx
    3f55:	4c 89 5c 24 30       	mov    %r11,0x30(%rsp)
    3f5a:	e8 11 ec ff ff       	callq  2b70 <__progname@@GLIBC_2.2.5-0x6510>
    3f5f:	48 83 c4 20          	add    $0x20,%rsp
    3f63:	4c 8b 5c 24 10       	mov    0x10(%rsp),%r11
    3f68:	49 39 c3             	cmp    %rax,%r11
    3f6b:	77 69                	ja     3fd6 <__progname@@GLIBC_2.2.5-0x50aa>
    3f6d:	48 8d 70 01          	lea    0x1(%rax),%rsi
    3f71:	48 8d 05 88 51 00 00 	lea    0x5188(%rip),%rax        # 9100 <stderr@@GLIBC_2.2.5+0x40>
    3f78:	48 89 33             	mov    %rsi,(%rbx)
    3f7b:	49 39 c4             	cmp    %rax,%r12
    3f7e:	74 13                	je     3f93 <__progname@@GLIBC_2.2.5-0x50ed>
    3f80:	48 89 74 24 10       	mov    %rsi,0x10(%rsp)
    3f85:	4c 89 e7             	mov    %r12,%rdi
    3f88:	ff 15 f2 4e 00 00    	callq  *0x4ef2(%rip)        # 8e80 <free@GLIBC_2.2.5>
    3f8e:	48 8b 74 24 10       	mov    0x10(%rsp),%rsi
    3f93:	48 89 74 24 10       	mov    %rsi,0x10(%rsp)
    3f98:	48 89 f7             	mov    %rsi,%rdi
    3f9b:	67 e8 ff 0e 00 00    	addr32 callq 4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    3fa1:	48 83 ec 08          	sub    $0x8,%rsp
    3fa5:	44 8b 45 00          	mov    0x0(%rbp),%r8d
    3fa9:	4c 89 f1             	mov    %r14,%rcx
    3fac:	48 89 43 08          	mov    %rax,0x8(%rbx)
    3fb0:	48 89 c7             	mov    %rax,%rdi
    3fb3:	49 89 c4             	mov    %rax,%r12
    3fb6:	ff 75 30             	pushq  0x30(%rbp)
    3fb9:	ff 75 28             	pushq  0x28(%rbp)
    3fbc:	41 57                	push   %r15
    3fbe:	44 8b 4c 24 3c       	mov    0x3c(%rsp),%r9d
    3fc3:	48 8b 54 24 28       	mov    0x28(%rsp),%rdx
    3fc8:	48 8b 74 24 30       	mov    0x30(%rsp),%rsi
    3fcd:	e8 9e eb ff ff       	callq  2b70 <__progname@@GLIBC_2.2.5-0x6510>
    3fd2:	48 83 c4 20          	add    $0x20,%rsp
    3fd6:	8b 44 24 18          	mov    0x18(%rsp),%eax
    3fda:	41 89 45 00          	mov    %eax,0x0(%r13)
    3fde:	48 83 c4 28          	add    $0x28,%rsp
    3fe2:	4c 89 e0             	mov    %r12,%rax
    3fe5:	5b                   	pop    %rbx
    3fe6:	5d                   	pop    %rbp
    3fe7:	41 5c                	pop    %r12
    3fe9:	41 5d                	pop    %r13
    3feb:	41 5e                	pop    %r14
    3fed:	41 5f                	pop    %r15
    3fef:	c3                   	retq   
    3ff0:	31 ff                	xor    %edi,%edi
    3ff2:	67 e8 08 0f 00 00    	addr32 callq 4f00 <__progname@@GLIBC_2.2.5-0x4180>
    3ff8:	66 0f 6f 05 70 50 00 	movdqa 0x5070(%rip),%xmm0        # 9070 <__progname@@GLIBC_2.2.5-0x10>
    3fff:	00 
    4000:	48 89 c3             	mov    %rax,%rbx
    4003:	48 89 05 56 50 00 00 	mov    %rax,0x5056(%rip)        # 9060 <__progname@@GLIBC_2.2.5-0x20>
    400a:	0f 11 00             	movups %xmm0,(%rax)
    400d:	e9 dd fe ff ff       	jmpq   3eef <__progname@@GLIBC_2.2.5-0x5191>
    4012:	67 e8 e8 10 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    4018:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    401f:	00 
    4020:	41 54                	push   %r12
    4022:	55                   	push   %rbp
    4023:	53                   	push   %rbx
    4024:	48 89 fb             	mov    %rdi,%rbx
    4027:	ff 15 63 4e 00 00    	callq  *0x4e63(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    402d:	48 85 db             	test   %rbx,%rbx
    4030:	be 38 00 00 00       	mov    $0x38,%esi
    4035:	44 8b 20             	mov    (%rax),%r12d
    4038:	48 89 c5             	mov    %rax,%rbp
    403b:	48 8d 05 be 51 00 00 	lea    0x51be(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    4042:	48 0f 44 d8          	cmove  %rax,%rbx
    4046:	48 89 df             	mov    %rbx,%rdi
    4049:	67 e8 61 10 00 00    	addr32 callq 50b0 <__progname@@GLIBC_2.2.5-0x3fd0>
    404f:	44 89 65 00          	mov    %r12d,0x0(%rbp)
    4053:	5b                   	pop    %rbx
    4054:	5d                   	pop    %rbp
    4055:	41 5c                	pop    %r12
    4057:	c3                   	retq   
    4058:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    405f:	00 
    4060:	48 85 ff             	test   %rdi,%rdi
    4063:	48 8d 05 96 51 00 00 	lea    0x5196(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    406a:	48 0f 44 f8          	cmove  %rax,%rdi
    406e:	8b 07                	mov    (%rdi),%eax
    4070:	c3                   	retq   
    4071:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    4078:	00 00 00 00 
    407c:	0f 1f 40 00          	nopl   0x0(%rax)
    4080:	48 85 ff             	test   %rdi,%rdi
    4083:	48 8d 05 76 51 00 00 	lea    0x5176(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    408a:	48 0f 44 f8          	cmove  %rax,%rdi
    408e:	89 37                	mov    %esi,(%rdi)
    4090:	c3                   	retq   
    4091:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    4098:	00 00 00 00 
    409c:	0f 1f 40 00          	nopl   0x0(%rax)
    40a0:	48 85 ff             	test   %rdi,%rdi
    40a3:	48 8d 05 56 51 00 00 	lea    0x5156(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    40aa:	89 f1                	mov    %esi,%ecx
    40ac:	48 0f 44 f8          	cmove  %rax,%rdi
    40b0:	89 f0                	mov    %esi,%eax
    40b2:	83 e1 1f             	and    $0x1f,%ecx
    40b5:	c0 e8 05             	shr    $0x5,%al
    40b8:	0f b6 c0             	movzbl %al,%eax
    40bb:	48 8d 7c 87 08       	lea    0x8(%rdi,%rax,4),%rdi
    40c0:	8b 37                	mov    (%rdi),%esi
    40c2:	89 f0                	mov    %esi,%eax
    40c4:	d3 e8                	shr    %cl,%eax
    40c6:	31 c2                	xor    %eax,%edx
    40c8:	83 e0 01             	and    $0x1,%eax
    40cb:	83 e2 01             	and    $0x1,%edx
    40ce:	d3 e2                	shl    %cl,%edx
    40d0:	31 f2                	xor    %esi,%edx
    40d2:	89 17                	mov    %edx,(%rdi)
    40d4:	c3                   	retq   
    40d5:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    40dc:	00 00 00 00 
    40e0:	48 85 ff             	test   %rdi,%rdi
    40e3:	48 8d 05 16 51 00 00 	lea    0x5116(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    40ea:	48 0f 44 f8          	cmove  %rax,%rdi
    40ee:	8b 47 04             	mov    0x4(%rdi),%eax
    40f1:	89 77 04             	mov    %esi,0x4(%rdi)
    40f4:	c3                   	retq   
    40f5:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    40fc:	00 00 00 00 
    4100:	48 85 ff             	test   %rdi,%rdi
    4103:	48 8d 05 f6 50 00 00 	lea    0x50f6(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    410a:	48 0f 44 f8          	cmove  %rax,%rdi
    410e:	c7 07 0a 00 00 00    	movl   $0xa,(%rdi)
    4114:	48 85 f6             	test   %rsi,%rsi
    4117:	74 0e                	je     4127 <__progname@@GLIBC_2.2.5-0x4f59>
    4119:	48 85 d2             	test   %rdx,%rdx
    411c:	74 09                	je     4127 <__progname@@GLIBC_2.2.5-0x4f59>
    411e:	48 89 77 28          	mov    %rsi,0x28(%rdi)
    4122:	48 89 57 30          	mov    %rdx,0x30(%rdi)
    4126:	c3                   	retq   
    4127:	50                   	push   %rax
    4128:	ff 15 5a 4d 00 00    	callq  *0x4d5a(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    412e:	66 90                	xchg   %ax,%ax
    4130:	41 57                	push   %r15
    4132:	48 8d 05 c7 50 00 00 	lea    0x50c7(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    4139:	49 89 d7             	mov    %rdx,%r15
    413c:	41 56                	push   %r14
    413e:	49 89 f6             	mov    %rsi,%r14
    4141:	41 55                	push   %r13
    4143:	49 89 fd             	mov    %rdi,%r13
    4146:	41 54                	push   %r12
    4148:	55                   	push   %rbp
    4149:	53                   	push   %rbx
    414a:	4c 89 c3             	mov    %r8,%rbx
    414d:	48 83 ec 18          	sub    $0x18,%rsp
    4151:	4d 85 c0             	test   %r8,%r8
    4154:	48 0f 44 d8          	cmove  %rax,%rbx
    4158:	48 89 4c 24 08       	mov    %rcx,0x8(%rsp)
    415d:	ff 15 2d 4d 00 00    	callq  *0x4d2d(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    4163:	48 83 ec 08          	sub    $0x8,%rsp
    4167:	4c 89 fa             	mov    %r15,%rdx
    416a:	4c 89 f6             	mov    %r14,%rsi
    416d:	44 8b 20             	mov    (%rax),%r12d
    4170:	48 89 c5             	mov    %rax,%rbp
    4173:	48 8d 43 08          	lea    0x8(%rbx),%rax
    4177:	44 8b 4b 04          	mov    0x4(%rbx),%r9d
    417b:	ff 73 30             	pushq  0x30(%rbx)
    417e:	44 8b 03             	mov    (%rbx),%r8d
    4181:	4c 89 ef             	mov    %r13,%rdi
    4184:	ff 73 28             	pushq  0x28(%rbx)
    4187:	50                   	push   %rax
    4188:	48 8b 4c 24 28       	mov    0x28(%rsp),%rcx
    418d:	e8 de e9 ff ff       	callq  2b70 <__progname@@GLIBC_2.2.5-0x6510>
    4192:	44 89 65 00          	mov    %r12d,0x0(%rbp)
    4196:	48 83 c4 38          	add    $0x38,%rsp
    419a:	5b                   	pop    %rbx
    419b:	5d                   	pop    %rbp
    419c:	41 5c                	pop    %r12
    419e:	41 5d                	pop    %r13
    41a0:	41 5e                	pop    %r14
    41a2:	41 5f                	pop    %r15
    41a4:	c3                   	retq   
    41a5:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    41ac:	00 00 00 00 
    41b0:	41 57                	push   %r15
    41b2:	48 8d 05 47 50 00 00 	lea    0x5047(%rip),%rax        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    41b9:	49 89 f7             	mov    %rsi,%r15
    41bc:	41 56                	push   %r14
    41be:	49 89 fe             	mov    %rdi,%r14
    41c1:	41 55                	push   %r13
    41c3:	41 54                	push   %r12
    41c5:	49 89 d4             	mov    %rdx,%r12
    41c8:	55                   	push   %rbp
    41c9:	53                   	push   %rbx
    41ca:	48 89 cb             	mov    %rcx,%rbx
    41cd:	48 83 ec 38          	sub    $0x38,%rsp
    41d1:	48 85 c9             	test   %rcx,%rcx
    41d4:	48 0f 44 d8          	cmove  %rax,%rbx
    41d8:	31 ed                	xor    %ebp,%ebp
    41da:	ff 15 b0 4c 00 00    	callq  *0x4cb0(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    41e0:	4d 85 e4             	test   %r12,%r12
    41e3:	4c 89 f9             	mov    %r15,%rcx
    41e6:	4c 89 f2             	mov    %r14,%rdx
    41e9:	49 89 c5             	mov    %rax,%r13
    41ec:	8b 00                	mov    (%rax),%eax
    41ee:	40 0f 94 c5          	sete   %bpl
    41f2:	4c 8d 53 08          	lea    0x8(%rbx),%r10
    41f6:	48 83 ec 08          	sub    $0x8,%rsp
    41fa:	0b 6b 04             	or     0x4(%rbx),%ebp
    41fd:	44 8b 03             	mov    (%rbx),%r8d
    4200:	31 f6                	xor    %esi,%esi
    4202:	89 44 24 14          	mov    %eax,0x14(%rsp)
    4206:	41 89 e9             	mov    %ebp,%r9d
    4209:	31 ff                	xor    %edi,%edi
    420b:	ff 73 30             	pushq  0x30(%rbx)
    420e:	ff 73 28             	pushq  0x28(%rbx)
    4211:	41 52                	push   %r10
    4213:	4c 89 54 24 40       	mov    %r10,0x40(%rsp)
    4218:	e8 53 e9 ff ff       	callq  2b70 <__progname@@GLIBC_2.2.5-0x6510>
    421d:	48 8d 70 01          	lea    0x1(%rax),%rsi
    4221:	48 89 44 24 48       	mov    %rax,0x48(%rsp)
    4226:	48 83 c4 20          	add    $0x20,%rsp
    422a:	48 89 f7             	mov    %rsi,%rdi
    422d:	48 89 74 24 18       	mov    %rsi,0x18(%rsp)
    4232:	67 e8 68 0c 00 00    	addr32 callq 4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    4238:	44 8b 03             	mov    (%rbx),%r8d
    423b:	41 89 e9             	mov    %ebp,%r9d
    423e:	4c 89 f9             	mov    %r15,%rcx
    4241:	48 89 44 24 10       	mov    %rax,0x10(%rsp)
    4246:	48 83 ec 08          	sub    $0x8,%rsp
    424a:	4c 89 f2             	mov    %r14,%rdx
    424d:	48 89 c7             	mov    %rax,%rdi
    4250:	ff 73 30             	pushq  0x30(%rbx)
    4253:	ff 73 28             	pushq  0x28(%rbx)
    4256:	4c 8b 54 24 38       	mov    0x38(%rsp),%r10
    425b:	41 52                	push   %r10
    425d:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
    4262:	e8 09 e9 ff ff       	callq  2b70 <__progname@@GLIBC_2.2.5-0x6510>
    4267:	8b 44 24 2c          	mov    0x2c(%rsp),%eax
    426b:	48 83 c4 20          	add    $0x20,%rsp
    426f:	41 89 45 00          	mov    %eax,0x0(%r13)
    4273:	4d 85 e4             	test   %r12,%r12
    4276:	74 09                	je     4281 <__progname@@GLIBC_2.2.5-0x4dff>
    4278:	4c 8b 5c 24 28       	mov    0x28(%rsp),%r11
    427d:	4d 89 1c 24          	mov    %r11,(%r12)
    4281:	48 8b 44 24 10       	mov    0x10(%rsp),%rax
    4286:	48 83 c4 38          	add    $0x38,%rsp
    428a:	5b                   	pop    %rbx
    428b:	5d                   	pop    %rbp
    428c:	41 5c                	pop    %r12
    428e:	41 5d                	pop    %r13
    4290:	41 5e                	pop    %r14
    4292:	41 5f                	pop    %r15
    4294:	c3                   	retq   
    4295:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    429c:	00 00 00 00 
    42a0:	48 89 d1             	mov    %rdx,%rcx
    42a3:	31 d2                	xor    %edx,%edx
    42a5:	e9 06 ff ff ff       	jmpq   41b0 <__progname@@GLIBC_2.2.5-0x4ed0>
    42aa:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    42b0:	8b 05 a2 4d 00 00    	mov    0x4da2(%rip),%eax        # 9058 <__progname@@GLIBC_2.2.5-0x28>
    42b6:	41 54                	push   %r12
    42b8:	4c 8b 25 a1 4d 00 00 	mov    0x4da1(%rip),%r12        # 9060 <__progname@@GLIBC_2.2.5-0x20>
    42bf:	55                   	push   %rbp
    42c0:	53                   	push   %rbx
    42c1:	83 f8 01             	cmp    $0x1,%eax
    42c4:	7e 2c                	jle    42f2 <__progname@@GLIBC_2.2.5-0x4d8e>
    42c6:	83 e8 02             	sub    $0x2,%eax
    42c9:	49 8d 5c 24 18       	lea    0x18(%r12),%rbx
    42ce:	48 c1 e0 04          	shl    $0x4,%rax
    42d2:	49 8d 6c 04 28       	lea    0x28(%r12,%rax,1),%rbp
    42d7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    42de:	00 00 
    42e0:	48 8b 3b             	mov    (%rbx),%rdi
    42e3:	48 83 c3 10          	add    $0x10,%rbx
    42e7:	ff 15 93 4b 00 00    	callq  *0x4b93(%rip)        # 8e80 <free@GLIBC_2.2.5>
    42ed:	48 39 eb             	cmp    %rbp,%rbx
    42f0:	75 ee                	jne    42e0 <__progname@@GLIBC_2.2.5-0x4da0>
    42f2:	49 8b 7c 24 08       	mov    0x8(%r12),%rdi
    42f7:	48 8d 1d 02 4e 00 00 	lea    0x4e02(%rip),%rbx        # 9100 <stderr@@GLIBC_2.2.5+0x40>
    42fe:	48 39 df             	cmp    %rbx,%rdi
    4301:	74 18                	je     431b <__progname@@GLIBC_2.2.5-0x4d65>
    4303:	ff 15 77 4b 00 00    	callq  *0x4b77(%rip)        # 8e80 <free@GLIBC_2.2.5>
    4309:	48 89 1d 68 4d 00 00 	mov    %rbx,0x4d68(%rip)        # 9078 <__progname@@GLIBC_2.2.5-0x8>
    4310:	48 c7 05 55 4d 00 00 	movq   $0x100,0x4d55(%rip)        # 9070 <__progname@@GLIBC_2.2.5-0x10>
    4317:	00 01 00 00 
    431b:	48 8d 1d 4e 4d 00 00 	lea    0x4d4e(%rip),%rbx        # 9070 <__progname@@GLIBC_2.2.5-0x10>
    4322:	49 39 dc             	cmp    %rbx,%r12
    4325:	74 10                	je     4337 <__progname@@GLIBC_2.2.5-0x4d49>
    4327:	4c 89 e7             	mov    %r12,%rdi
    432a:	ff 15 50 4b 00 00    	callq  *0x4b50(%rip)        # 8e80 <free@GLIBC_2.2.5>
    4330:	48 89 1d 29 4d 00 00 	mov    %rbx,0x4d29(%rip)        # 9060 <__progname@@GLIBC_2.2.5-0x20>
    4337:	c7 05 17 4d 00 00 01 	movl   $0x1,0x4d17(%rip)        # 9058 <__progname@@GLIBC_2.2.5-0x28>
    433e:	00 00 00 
    4341:	5b                   	pop    %rbx
    4342:	5d                   	pop    %rbp
    4343:	41 5c                	pop    %r12
    4345:	c3                   	retq   
    4346:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    434d:	00 00 00 
    4350:	48 8d 0d a9 4e 00 00 	lea    0x4ea9(%rip),%rcx        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    4357:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    435e:	e9 0d fb ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    4363:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    436a:	00 00 00 00 
    436e:	66 90                	xchg   %ax,%ax
    4370:	48 8d 0d 89 4e 00 00 	lea    0x4e89(%rip),%rcx        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    4377:	e9 f4 fa ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    437c:	0f 1f 40 00          	nopl   0x0(%rax)
    4380:	48 89 fe             	mov    %rdi,%rsi
    4383:	48 8d 0d 76 4e 00 00 	lea    0x4e76(%rip),%rcx        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    438a:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    4391:	31 ff                	xor    %edi,%edi
    4393:	e9 d8 fa ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    4398:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    439f:	00 
    43a0:	48 89 f2             	mov    %rsi,%rdx
    43a3:	48 8d 0d 56 4e 00 00 	lea    0x4e56(%rip),%rcx        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    43aa:	48 89 fe             	mov    %rdi,%rsi
    43ad:	31 ff                	xor    %edi,%edi
    43af:	e9 bc fa ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    43b4:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    43bb:	00 00 00 00 
    43bf:	90                   	nop
    43c0:	48 83 ec 48          	sub    $0x48,%rsp
    43c4:	48 89 d0             	mov    %rdx,%rax
    43c7:	64 48 8b 14 25 28 00 	mov    %fs:0x28,%rdx
    43ce:	00 00 
    43d0:	48 89 54 24 38       	mov    %rdx,0x38(%rsp)
    43d5:	31 d2                	xor    %edx,%edx
    43d7:	83 fe 0a             	cmp    $0xa,%esi
    43da:	0f 84 4c dc ff ff    	je     202c <__progname@@GLIBC_2.2.5-0x7054>
    43e0:	89 34 24             	mov    %esi,(%rsp)
    43e3:	48 89 e1             	mov    %rsp,%rcx
    43e6:	48 89 c6             	mov    %rax,%rsi
    43e9:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    43f0:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%rsp)
    43f7:	00 
    43f8:	48 c7 44 24 08 00 00 	movq   $0x0,0x8(%rsp)
    43ff:	00 00 
    4401:	48 c7 44 24 10 00 00 	movq   $0x0,0x10(%rsp)
    4408:	00 00 
    440a:	48 c7 44 24 18 00 00 	movq   $0x0,0x18(%rsp)
    4411:	00 00 
    4413:	48 c7 44 24 20 00 00 	movq   $0x0,0x20(%rsp)
    441a:	00 00 
    441c:	48 c7 44 24 28 00 00 	movq   $0x0,0x28(%rsp)
    4423:	00 00 
    4425:	48 c7 44 24 30 00 00 	movq   $0x0,0x30(%rsp)
    442c:	00 00 
    442e:	e8 3d fa ff ff       	callq  3e70 <__progname@@GLIBC_2.2.5-0x5210>
    4433:	48 8b 4c 24 38       	mov    0x38(%rsp),%rcx
    4438:	64 48 33 0c 25 28 00 	xor    %fs:0x28,%rcx
    443f:	00 00 
    4441:	75 05                	jne    4448 <__progname@@GLIBC_2.2.5-0x4c38>
    4443:	48 83 c4 48          	add    $0x48,%rsp
    4447:	c3                   	retq   
    4448:	ff 15 a2 4a 00 00    	callq  *0x4aa2(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    444e:	66 90                	xchg   %ax,%ax
    4450:	48 83 ec 48          	sub    $0x48,%rsp
    4454:	48 89 d0             	mov    %rdx,%rax
    4457:	48 89 ca             	mov    %rcx,%rdx
    445a:	64 48 8b 0c 25 28 00 	mov    %fs:0x28,%rcx
    4461:	00 00 
    4463:	48 89 4c 24 38       	mov    %rcx,0x38(%rsp)
    4468:	31 c9                	xor    %ecx,%ecx
    446a:	83 fe 0a             	cmp    $0xa,%esi
    446d:	0f 84 bf db ff ff    	je     2032 <__progname@@GLIBC_2.2.5-0x704e>
    4473:	89 34 24             	mov    %esi,(%rsp)
    4476:	48 89 e1             	mov    %rsp,%rcx
    4479:	48 89 c6             	mov    %rax,%rsi
    447c:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%rsp)
    4483:	00 
    4484:	48 c7 44 24 08 00 00 	movq   $0x0,0x8(%rsp)
    448b:	00 00 
    448d:	48 c7 44 24 10 00 00 	movq   $0x0,0x10(%rsp)
    4494:	00 00 
    4496:	48 c7 44 24 18 00 00 	movq   $0x0,0x18(%rsp)
    449d:	00 00 
    449f:	48 c7 44 24 20 00 00 	movq   $0x0,0x20(%rsp)
    44a6:	00 00 
    44a8:	48 c7 44 24 28 00 00 	movq   $0x0,0x28(%rsp)
    44af:	00 00 
    44b1:	48 c7 44 24 30 00 00 	movq   $0x0,0x30(%rsp)
    44b8:	00 00 
    44ba:	e8 b1 f9 ff ff       	callq  3e70 <__progname@@GLIBC_2.2.5-0x5210>
    44bf:	48 8b 54 24 38       	mov    0x38(%rsp),%rdx
    44c4:	64 48 33 14 25 28 00 	xor    %fs:0x28,%rdx
    44cb:	00 00 
    44cd:	75 05                	jne    44d4 <__progname@@GLIBC_2.2.5-0x4bac>
    44cf:	48 83 c4 48          	add    $0x48,%rsp
    44d3:	c3                   	retq   
    44d4:	ff 15 16 4a 00 00    	callq  *0x4a16(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    44da:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    44e0:	48 89 f2             	mov    %rsi,%rdx
    44e3:	89 fe                	mov    %edi,%esi
    44e5:	31 ff                	xor    %edi,%edi
    44e7:	e9 d4 fe ff ff       	jmpq   43c0 <__progname@@GLIBC_2.2.5-0x4cc0>
    44ec:	0f 1f 40 00          	nopl   0x0(%rax)
    44f0:	48 89 d1             	mov    %rdx,%rcx
    44f3:	48 89 f2             	mov    %rsi,%rdx
    44f6:	89 fe                	mov    %edi,%esi
    44f8:	31 ff                	xor    %edi,%edi
    44fa:	e9 51 ff ff ff       	jmpq   4450 <__progname@@GLIBC_2.2.5-0x4c30>
    44ff:	90                   	nop
    4500:	48 83 ec 48          	sub    $0x48,%rsp
    4504:	66 0f 6f 05 f4 4c 00 	movdqa 0x4cf4(%rip),%xmm0        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    450b:	00 
    450c:	66 0f 6f 0d fc 4c 00 	movdqa 0x4cfc(%rip),%xmm1        # 9210 <stderr@@GLIBC_2.2.5+0x150>
    4513:	00 
    4514:	89 d1                	mov    %edx,%ecx
    4516:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    451d:	00 00 
    451f:	48 89 44 24 38       	mov    %rax,0x38(%rsp)
    4524:	31 c0                	xor    %eax,%eax
    4526:	48 8b 05 03 4d 00 00 	mov    0x4d03(%rip),%rax        # 9230 <stderr@@GLIBC_2.2.5+0x170>
    452d:	49 89 e0             	mov    %rsp,%r8
    4530:	83 e1 1f             	and    $0x1f,%ecx
    4533:	66 0f 6f 15 e5 4c 00 	movdqa 0x4ce5(%rip),%xmm2        # 9220 <stderr@@GLIBC_2.2.5+0x160>
    453a:	00 
    453b:	0f 29 04 24          	movaps %xmm0,(%rsp)
    453f:	48 89 44 24 30       	mov    %rax,0x30(%rsp)
    4544:	89 d0                	mov    %edx,%eax
    4546:	c0 e8 05             	shr    $0x5,%al
    4549:	0f 29 4c 24 10       	movaps %xmm1,0x10(%rsp)
    454e:	0f b6 c0             	movzbl %al,%eax
    4551:	0f 29 54 24 20       	movaps %xmm2,0x20(%rsp)
    4556:	4d 8d 4c 80 08       	lea    0x8(%r8,%rax,4),%r9
    455b:	41 8b 11             	mov    (%r9),%edx
    455e:	89 d0                	mov    %edx,%eax
    4560:	d3 e8                	shr    %cl,%eax
    4562:	f7 d0                	not    %eax
    4564:	83 e0 01             	and    $0x1,%eax
    4567:	d3 e0                	shl    %cl,%eax
    4569:	4c 89 c1             	mov    %r8,%rcx
    456c:	31 d0                	xor    %edx,%eax
    456e:	48 89 f2             	mov    %rsi,%rdx
    4571:	48 89 fe             	mov    %rdi,%rsi
    4574:	31 ff                	xor    %edi,%edi
    4576:	41 89 01             	mov    %eax,(%r9)
    4579:	e8 f2 f8 ff ff       	callq  3e70 <__progname@@GLIBC_2.2.5-0x5210>
    457e:	48 8b 74 24 38       	mov    0x38(%rsp),%rsi
    4583:	64 48 33 34 25 28 00 	xor    %fs:0x28,%rsi
    458a:	00 00 
    458c:	75 05                	jne    4593 <__progname@@GLIBC_2.2.5-0x4aed>
    458e:	48 83 c4 48          	add    $0x48,%rsp
    4592:	c3                   	retq   
    4593:	ff 15 57 49 00 00    	callq  *0x4957(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    4599:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    45a0:	40 0f be d6          	movsbl %sil,%edx
    45a4:	48 c7 c6 ff ff ff ff 	mov    $0xffffffffffffffff,%rsi
    45ab:	e9 50 ff ff ff       	jmpq   4500 <__progname@@GLIBC_2.2.5-0x4b80>
    45b0:	ba 3a 00 00 00       	mov    $0x3a,%edx
    45b5:	48 c7 c6 ff ff ff ff 	mov    $0xffffffffffffffff,%rsi
    45bc:	e9 3f ff ff ff       	jmpq   4500 <__progname@@GLIBC_2.2.5-0x4b80>
    45c1:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    45c8:	00 00 00 00 
    45cc:	0f 1f 40 00          	nopl   0x0(%rax)
    45d0:	ba 3a 00 00 00       	mov    $0x3a,%edx
    45d5:	e9 26 ff ff ff       	jmpq   4500 <__progname@@GLIBC_2.2.5-0x4b80>
    45da:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    45e0:	48 83 ec 48          	sub    $0x48,%rsp
    45e4:	64 48 8b 0c 25 28 00 	mov    %fs:0x28,%rcx
    45eb:	00 00 
    45ed:	48 89 4c 24 38       	mov    %rcx,0x38(%rsp)
    45f2:	31 c9                	xor    %ecx,%ecx
    45f4:	83 fe 0a             	cmp    $0xa,%esi
    45f7:	0f 84 3b da ff ff    	je     2038 <__progname@@GLIBC_2.2.5-0x7048>
    45fd:	48 89 d0             	mov    %rdx,%rax
    4600:	89 34 24             	mov    %esi,(%rsp)
    4603:	48 ba 00 00 00 00 00 	movabs $0x400000000000000,%rdx
    460a:	00 00 04 
    460d:	48 89 e1             	mov    %rsp,%rcx
    4610:	48 89 54 24 08       	mov    %rdx,0x8(%rsp)
    4615:	48 89 c6             	mov    %rax,%rsi
    4618:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    461f:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%rsp)
    4626:	00 
    4627:	48 c7 44 24 10 00 00 	movq   $0x0,0x10(%rsp)
    462e:	00 00 
    4630:	48 c7 44 24 18 00 00 	movq   $0x0,0x18(%rsp)
    4637:	00 00 
    4639:	48 c7 44 24 20 00 00 	movq   $0x0,0x20(%rsp)
    4640:	00 00 
    4642:	48 c7 44 24 28 00 00 	movq   $0x0,0x28(%rsp)
    4649:	00 00 
    464b:	48 c7 44 24 30 00 00 	movq   $0x0,0x30(%rsp)
    4652:	00 00 
    4654:	e8 17 f8 ff ff       	callq  3e70 <__progname@@GLIBC_2.2.5-0x5210>
    4659:	48 8b 54 24 38       	mov    0x38(%rsp),%rdx
    465e:	64 48 33 14 25 28 00 	xor    %fs:0x28,%rdx
    4665:	00 00 
    4667:	75 05                	jne    466e <__progname@@GLIBC_2.2.5-0x4a12>
    4669:	48 83 c4 48          	add    $0x48,%rsp
    466d:	c3                   	retq   
    466e:	ff 15 7c 48 00 00    	callq  *0x487c(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    4674:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    467b:	00 00 00 00 
    467f:	90                   	nop
    4680:	48 83 ec 48          	sub    $0x48,%rsp
    4684:	49 89 c9             	mov    %rcx,%r9
    4687:	66 0f 6f 05 71 4b 00 	movdqa 0x4b71(%rip),%xmm0        # 9200 <stderr@@GLIBC_2.2.5+0x140>
    468e:	00 
    468f:	66 0f 6f 0d 79 4b 00 	movdqa 0x4b79(%rip),%xmm1        # 9210 <stderr@@GLIBC_2.2.5+0x150>
    4696:	00 
    4697:	66 0f 6f 15 81 4b 00 	movdqa 0x4b81(%rip),%xmm2        # 9220 <stderr@@GLIBC_2.2.5+0x160>
    469e:	00 
    469f:	48 8b 0d 8a 4b 00 00 	mov    0x4b8a(%rip),%rcx        # 9230 <stderr@@GLIBC_2.2.5+0x170>
    46a6:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    46ad:	00 00 
    46af:	48 89 44 24 38       	mov    %rax,0x38(%rsp)
    46b4:	31 c0                	xor    %eax,%eax
    46b6:	0f 29 04 24          	movaps %xmm0,(%rsp)
    46ba:	0f 29 4c 24 10       	movaps %xmm1,0x10(%rsp)
    46bf:	0f 29 54 24 20       	movaps %xmm2,0x20(%rsp)
    46c4:	48 89 4c 24 30       	mov    %rcx,0x30(%rsp)
    46c9:	c7 04 24 0a 00 00 00 	movl   $0xa,(%rsp)
    46d0:	48 85 f6             	test   %rsi,%rsi
    46d3:	74 38                	je     470d <__progname@@GLIBC_2.2.5-0x4973>
    46d5:	48 85 d2             	test   %rdx,%rdx
    46d8:	74 33                	je     470d <__progname@@GLIBC_2.2.5-0x4973>
    46da:	48 89 74 24 28       	mov    %rsi,0x28(%rsp)
    46df:	48 89 e1             	mov    %rsp,%rcx
    46e2:	4c 89 ce             	mov    %r9,%rsi
    46e5:	48 89 54 24 30       	mov    %rdx,0x30(%rsp)
    46ea:	4c 89 c2             	mov    %r8,%rdx
    46ed:	e8 7e f7 ff ff       	callq  3e70 <__progname@@GLIBC_2.2.5-0x5210>
    46f2:	48 8b 7c 24 38       	mov    0x38(%rsp),%rdi
    46f7:	64 48 33 3c 25 28 00 	xor    %fs:0x28,%rdi
    46fe:	00 00 
    4700:	75 05                	jne    4707 <__progname@@GLIBC_2.2.5-0x4979>
    4702:	48 83 c4 48          	add    $0x48,%rsp
    4706:	c3                   	retq   
    4707:	ff 15 e3 47 00 00    	callq  *0x47e3(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    470d:	ff 15 75 47 00 00    	callq  *0x4775(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    4713:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    471a:	00 00 00 00 
    471e:	66 90                	xchg   %ax,%ax
    4720:	49 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%r8
    4727:	e9 54 ff ff ff       	jmpq   4680 <__progname@@GLIBC_2.2.5-0x4a00>
    472c:	0f 1f 40 00          	nopl   0x0(%rax)
    4730:	48 89 d1             	mov    %rdx,%rcx
    4733:	49 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%r8
    473a:	48 89 f2             	mov    %rsi,%rdx
    473d:	48 89 fe             	mov    %rdi,%rsi
    4740:	31 ff                	xor    %edi,%edi
    4742:	e9 39 ff ff ff       	jmpq   4680 <__progname@@GLIBC_2.2.5-0x4a00>
    4747:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    474e:	00 00 
    4750:	49 89 c8             	mov    %rcx,%r8
    4753:	48 89 d1             	mov    %rdx,%rcx
    4756:	48 89 f2             	mov    %rsi,%rdx
    4759:	48 89 fe             	mov    %rdi,%rsi
    475c:	31 ff                	xor    %edi,%edi
    475e:	e9 1d ff ff ff       	jmpq   4680 <__progname@@GLIBC_2.2.5-0x4a00>
    4763:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    476a:	00 00 00 00 
    476e:	66 90                	xchg   %ax,%ax
    4770:	48 8d 0d a9 48 00 00 	lea    0x48a9(%rip),%rcx        # 9020 <__progname@@GLIBC_2.2.5-0x60>
    4777:	e9 f4 f6 ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    477c:	0f 1f 40 00          	nopl   0x0(%rax)
    4780:	48 89 f2             	mov    %rsi,%rdx
    4783:	48 8d 0d 96 48 00 00 	lea    0x4896(%rip),%rcx        # 9020 <__progname@@GLIBC_2.2.5-0x60>
    478a:	48 89 fe             	mov    %rdi,%rsi
    478d:	31 ff                	xor    %edi,%edi
    478f:	e9 dc f6 ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    4794:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    479b:	00 00 00 00 
    479f:	90                   	nop
    47a0:	48 8d 0d 79 48 00 00 	lea    0x4879(%rip),%rcx        # 9020 <__progname@@GLIBC_2.2.5-0x60>
    47a7:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    47ae:	e9 bd f6 ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    47b3:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    47ba:	00 00 00 00 
    47be:	66 90                	xchg   %ax,%ax
    47c0:	48 89 fe             	mov    %rdi,%rsi
    47c3:	48 8d 0d 56 48 00 00 	lea    0x4856(%rip),%rcx        # 9020 <__progname@@GLIBC_2.2.5-0x60>
    47ca:	48 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%rdx
    47d1:	31 ff                	xor    %edi,%edi
    47d3:	e9 98 f6 ff ff       	jmpq   3e70 <__progname@@GLIBC_2.2.5-0x5210>
    47d8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    47df:	00 
    47e0:	41 55                	push   %r13
    47e2:	41 89 fd             	mov    %edi,%r13d
    47e5:	41 54                	push   %r12
    47e7:	49 89 f4             	mov    %rsi,%r12
    47ea:	55                   	push   %rbp
    47eb:	53                   	push   %rbx
    47ec:	48 89 d3             	mov    %rdx,%rbx
    47ef:	48 83 ec 08          	sub    $0x8,%rsp
    47f3:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    47f8:	48 89 da             	mov    %rbx,%rdx
    47fb:	4c 89 e6             	mov    %r12,%rsi
    47fe:	44 89 ef             	mov    %r13d,%edi
    4801:	ff 15 b1 46 00 00    	callq  *0x46b1(%rip)        # 8eb8 <write@GLIBC_2.2.5>
    4807:	48 89 c5             	mov    %rax,%rbp
    480a:	48 85 c0             	test   %rax,%rax
    480d:	79 29                	jns    4838 <__progname@@GLIBC_2.2.5-0x4848>
    480f:	ff 15 7b 46 00 00    	callq  *0x467b(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    4815:	8b 00                	mov    (%rax),%eax
    4817:	83 f8 04             	cmp    $0x4,%eax
    481a:	74 dc                	je     47f8 <__progname@@GLIBC_2.2.5-0x4888>
    481c:	83 f8 16             	cmp    $0x16,%eax
    481f:	75 17                	jne    4838 <__progname@@GLIBC_2.2.5-0x4848>
    4821:	48 81 fb 00 00 f0 7f 	cmp    $0x7ff00000,%rbx
    4828:	76 0e                	jbe    4838 <__progname@@GLIBC_2.2.5-0x4848>
    482a:	bb 00 00 f0 7f       	mov    $0x7ff00000,%ebx
    482f:	eb c7                	jmp    47f8 <__progname@@GLIBC_2.2.5-0x4888>
    4831:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    4838:	48 83 c4 08          	add    $0x8,%rsp
    483c:	48 89 e8             	mov    %rbp,%rax
    483f:	5b                   	pop    %rbx
    4840:	5d                   	pop    %rbp
    4841:	41 5c                	pop    %r12
    4843:	41 5d                	pop    %r13
    4845:	c3                   	retq   
    4846:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    484d:	00 00 00 
    4850:	41 57                	push   %r15
    4852:	41 56                	push   %r14
    4854:	41 55                	push   %r13
    4856:	41 54                	push   %r12
    4858:	4d 89 cc             	mov    %r9,%r12
    485b:	55                   	push   %rbp
    485c:	48 89 fd             	mov    %rdi,%rbp
    485f:	53                   	push   %rbx
    4860:	4c 89 c3             	mov    %r8,%rbx
    4863:	48 83 ec 28          	sub    $0x28,%rsp
    4867:	48 85 f6             	test   %rsi,%rsi
    486a:	0f 84 90 00 00 00    	je     4900 <__progname@@GLIBC_2.2.5-0x4780>
    4870:	49 89 c9             	mov    %rcx,%r9
    4873:	49 89 d0             	mov    %rdx,%r8
    4876:	48 89 f1             	mov    %rsi,%rcx
    4879:	31 c0                	xor    %eax,%eax
    487b:	48 8d 15 66 21 00 00 	lea    0x2166(%rip),%rdx        # 69e8 <__progname@@GLIBC_2.2.5-0x2698>
    4882:	be 01 00 00 00       	mov    $0x1,%esi
    4887:	ff 15 2b 47 00 00    	callq  *0x472b(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    488d:	31 ff                	xor    %edi,%edi
    488f:	ba 05 00 00 00       	mov    $0x5,%edx
    4894:	48 8d 35 60 21 00 00 	lea    0x2160(%rip),%rsi        # 69fb <__progname@@GLIBC_2.2.5-0x2685>
    489b:	ff 15 37 46 00 00    	callq  *0x4637(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    48a1:	41 b8 e2 07 00 00    	mov    $0x7e2,%r8d
    48a7:	be 01 00 00 00       	mov    $0x1,%esi
    48ac:	48 89 ef             	mov    %rbp,%rdi
    48af:	48 89 c1             	mov    %rax,%rcx
    48b2:	48 8d 15 67 24 00 00 	lea    0x2467(%rip),%rdx        # 6d20 <__progname@@GLIBC_2.2.5-0x2360>
    48b9:	31 c0                	xor    %eax,%eax
    48bb:	ff 15 f7 46 00 00    	callq  *0x46f7(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    48c1:	31 ff                	xor    %edi,%edi
    48c3:	ba 05 00 00 00       	mov    $0x5,%edx
    48c8:	48 8d 35 b9 21 00 00 	lea    0x21b9(%rip),%rsi        # 6a88 <__progname@@GLIBC_2.2.5-0x25f8>
    48cf:	ff 15 03 46 00 00    	callq  *0x4603(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    48d5:	48 89 ee             	mov    %rbp,%rsi
    48d8:	48 89 c7             	mov    %rax,%rdi
    48db:	ff 15 4f 46 00 00    	callq  *0x464f(%rip)        # 8f30 <fputs_unlocked@GLIBC_2.2.5>
    48e1:	49 83 fc 09          	cmp    $0x9,%r12
    48e5:	0f 87 45 03 00 00    	ja     4c30 <__progname@@GLIBC_2.2.5-0x4450>
    48eb:	48 8d 15 f6 23 00 00 	lea    0x23f6(%rip),%rdx        # 6ce8 <__progname@@GLIBC_2.2.5-0x2398>
    48f2:	4a 63 04 a2          	movslq (%rdx,%r12,4),%rax
    48f6:	48 01 d0             	add    %rdx,%rax
    48f9:	ff e0                	jmpq   *%rax
    48fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    4900:	49 89 c8             	mov    %rcx,%r8
    4903:	be 01 00 00 00       	mov    $0x1,%esi
    4908:	48 89 d1             	mov    %rdx,%rcx
    490b:	31 c0                	xor    %eax,%eax
    490d:	48 8d 15 e0 20 00 00 	lea    0x20e0(%rip),%rdx        # 69f4 <__progname@@GLIBC_2.2.5-0x268c>
    4914:	ff 15 9e 46 00 00    	callq  *0x469e(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    491a:	e9 6e ff ff ff       	jmpq   488d <__progname@@GLIBC_2.2.5-0x47f3>
    491f:	90                   	nop
    4920:	4c 8b 4b 38          	mov    0x38(%rbx),%r9
    4924:	48 8b 43 10          	mov    0x10(%rbx),%rax
    4928:	ba 05 00 00 00       	mov    $0x5,%edx
    492d:	31 ff                	xor    %edi,%edi
    492f:	4c 8b 43 08          	mov    0x8(%rbx),%r8
    4933:	4c 8b 6b 30          	mov    0x30(%rbx),%r13
    4937:	48 8d 35 ba 22 00 00 	lea    0x22ba(%rip),%rsi        # 6bf8 <__progname@@GLIBC_2.2.5-0x2488>
    493e:	4c 8b 63 28          	mov    0x28(%rbx),%r12
    4942:	4c 8b 7b 20          	mov    0x20(%rbx),%r15
    4946:	4c 89 4c 24 10       	mov    %r9,0x10(%rsp)
    494b:	4c 8b 73 18          	mov    0x18(%rbx),%r14
    494f:	48 8b 1b             	mov    (%rbx),%rbx
    4952:	48 89 04 24          	mov    %rax,(%rsp)
    4956:	4c 89 44 24 08       	mov    %r8,0x8(%rsp)
    495b:	ff 15 77 45 00 00    	callq  *0x4577(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4961:	48 83 ec 08          	sub    $0x8,%rsp
    4965:	4c 8b 4c 24 18       	mov    0x18(%rsp),%r9
    496a:	48 89 d9             	mov    %rbx,%rcx
    496d:	48 89 c2             	mov    %rax,%rdx
    4970:	48 89 ef             	mov    %rbp,%rdi
    4973:	be 01 00 00 00       	mov    $0x1,%esi
    4978:	31 c0                	xor    %eax,%eax
    497a:	41 51                	push   %r9
    497c:	41 55                	push   %r13
    497e:	41 54                	push   %r12
    4980:	41 57                	push   %r15
    4982:	41 56                	push   %r14
    4984:	4c 8b 4c 24 30       	mov    0x30(%rsp),%r9
    4989:	4c 8b 44 24 38       	mov    0x38(%rsp),%r8
    498e:	ff 15 24 46 00 00    	callq  *0x4624(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    4994:	48 83 c4 30          	add    $0x30,%rsp
    4998:	48 83 c4 28          	add    $0x28,%rsp
    499c:	5b                   	pop    %rbx
    499d:	5d                   	pop    %rbp
    499e:	41 5c                	pop    %r12
    49a0:	41 5d                	pop    %r13
    49a2:	41 5e                	pop    %r14
    49a4:	41 5f                	pop    %r15
    49a6:	c3                   	retq   
    49a7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    49ae:	00 00 
    49b0:	4c 8b 53 40          	mov    0x40(%rbx),%r10
    49b4:	4c 8b 4b 38          	mov    0x38(%rbx),%r9
    49b8:	ba 05 00 00 00       	mov    $0x5,%edx
    49bd:	48 8d 35 64 22 00 00 	lea    0x2264(%rip),%rsi        # 6c28 <__progname@@GLIBC_2.2.5-0x2458>
    49c4:	48 8b 43 10          	mov    0x10(%rbx),%rax
    49c8:	4c 8b 43 08          	mov    0x8(%rbx),%r8
    49cc:	4c 8b 6b 30          	mov    0x30(%rbx),%r13
    49d0:	4c 8b 63 28          	mov    0x28(%rbx),%r12
    49d4:	4c 89 54 24 18       	mov    %r10,0x18(%rsp)
    49d9:	4c 8b 7b 20          	mov    0x20(%rbx),%r15
    49dd:	4c 8b 73 18          	mov    0x18(%rbx),%r14
    49e1:	4c 89 4c 24 10       	mov    %r9,0x10(%rsp)
    49e6:	48 89 04 24          	mov    %rax,(%rsp)
    49ea:	48 8b 1b             	mov    (%rbx),%rbx
    49ed:	4c 89 44 24 08       	mov    %r8,0x8(%rsp)
    49f2:	31 ff                	xor    %edi,%edi
    49f4:	ff 15 de 44 00 00    	callq  *0x44de(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    49fa:	4c 8b 54 24 18       	mov    0x18(%rsp),%r10
    49ff:	41 52                	push   %r10
    4a01:	e9 5f ff ff ff       	jmpq   4965 <__progname@@GLIBC_2.2.5-0x471b>
    4a06:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    4a0d:	00 00 00 
    4a10:	48 8b 1b             	mov    (%rbx),%rbx
    4a13:	ba 05 00 00 00       	mov    $0x5,%edx
    4a18:	48 8d 35 e0 1f 00 00 	lea    0x1fe0(%rip),%rsi        # 69ff <__progname@@GLIBC_2.2.5-0x2681>
    4a1f:	31 ff                	xor    %edi,%edi
    4a21:	ff 15 b1 44 00 00    	callq  *0x44b1(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4a27:	48 83 c4 28          	add    $0x28,%rsp
    4a2b:	48 89 ef             	mov    %rbp,%rdi
    4a2e:	be 01 00 00 00       	mov    $0x1,%esi
    4a33:	48 89 d9             	mov    %rbx,%rcx
    4a36:	48 89 c2             	mov    %rax,%rdx
    4a39:	5b                   	pop    %rbx
    4a3a:	31 c0                	xor    %eax,%eax
    4a3c:	5d                   	pop    %rbp
    4a3d:	41 5c                	pop    %r12
    4a3f:	41 5d                	pop    %r13
    4a41:	41 5e                	pop    %r14
    4a43:	41 5f                	pop    %r15
    4a45:	ff 25 6d 45 00 00    	jmpq   *0x456d(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    4a4b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    4a50:	4c 8b 63 08          	mov    0x8(%rbx),%r12
    4a54:	48 8b 1b             	mov    (%rbx),%rbx
    4a57:	ba 05 00 00 00       	mov    $0x5,%edx
    4a5c:	31 ff                	xor    %edi,%edi
    4a5e:	48 8d 35 aa 1f 00 00 	lea    0x1faa(%rip),%rsi        # 6a0f <__progname@@GLIBC_2.2.5-0x2671>
    4a65:	ff 15 6d 44 00 00    	callq  *0x446d(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4a6b:	48 83 c4 28          	add    $0x28,%rsp
    4a6f:	4d 89 e0             	mov    %r12,%r8
    4a72:	48 89 d9             	mov    %rbx,%rcx
    4a75:	48 89 c2             	mov    %rax,%rdx
    4a78:	5b                   	pop    %rbx
    4a79:	48 89 ef             	mov    %rbp,%rdi
    4a7c:	be 01 00 00 00       	mov    $0x1,%esi
    4a81:	5d                   	pop    %rbp
    4a82:	31 c0                	xor    %eax,%eax
    4a84:	41 5c                	pop    %r12
    4a86:	41 5d                	pop    %r13
    4a88:	41 5e                	pop    %r14
    4a8a:	41 5f                	pop    %r15
    4a8c:	ff 25 26 45 00 00    	jmpq   *0x4526(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    4a92:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    4a98:	4c 8b 6b 10          	mov    0x10(%rbx),%r13
    4a9c:	4c 8b 63 08          	mov    0x8(%rbx),%r12
    4aa0:	ba 05 00 00 00       	mov    $0x5,%edx
    4aa5:	31 ff                	xor    %edi,%edi
    4aa7:	48 8b 1b             	mov    (%rbx),%rbx
    4aaa:	48 8d 35 75 1f 00 00 	lea    0x1f75(%rip),%rsi        # 6a26 <__progname@@GLIBC_2.2.5-0x265a>
    4ab1:	ff 15 21 44 00 00    	callq  *0x4421(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4ab7:	48 83 c4 28          	add    $0x28,%rsp
    4abb:	4d 89 e9             	mov    %r13,%r9
    4abe:	4d 89 e0             	mov    %r12,%r8
    4ac1:	48 89 d9             	mov    %rbx,%rcx
    4ac4:	48 89 c2             	mov    %rax,%rdx
    4ac7:	5b                   	pop    %rbx
    4ac8:	48 89 ef             	mov    %rbp,%rdi
    4acb:	be 01 00 00 00       	mov    $0x1,%esi
    4ad0:	5d                   	pop    %rbp
    4ad1:	31 c0                	xor    %eax,%eax
    4ad3:	41 5c                	pop    %r12
    4ad5:	41 5d                	pop    %r13
    4ad7:	41 5e                	pop    %r14
    4ad9:	41 5f                	pop    %r15
    4adb:	ff 25 d7 44 00 00    	jmpq   *0x44d7(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    4ae1:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    4ae8:	4c 8b 73 18          	mov    0x18(%rbx),%r14
    4aec:	4c 8b 6b 10          	mov    0x10(%rbx),%r13
    4af0:	ba 05 00 00 00       	mov    $0x5,%edx
    4af5:	31 ff                	xor    %edi,%edi
    4af7:	4c 8b 63 08          	mov    0x8(%rbx),%r12
    4afb:	48 8d 35 56 20 00 00 	lea    0x2056(%rip),%rsi        # 6b58 <__progname@@GLIBC_2.2.5-0x2528>
    4b02:	48 8b 1b             	mov    (%rbx),%rbx
    4b05:	ff 15 cd 43 00 00    	callq  *0x43cd(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4b0b:	48 83 ec 08          	sub    $0x8,%rsp
    4b0f:	41 56                	push   %r14
    4b11:	48 89 c2             	mov    %rax,%rdx
    4b14:	4d 89 e9             	mov    %r13,%r9
    4b17:	4d 89 e0             	mov    %r12,%r8
    4b1a:	48 89 d9             	mov    %rbx,%rcx
    4b1d:	48 89 ef             	mov    %rbp,%rdi
    4b20:	be 01 00 00 00       	mov    $0x1,%esi
    4b25:	31 c0                	xor    %eax,%eax
    4b27:	ff 15 8b 44 00 00    	callq  *0x448b(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    4b2d:	58                   	pop    %rax
    4b2e:	5a                   	pop    %rdx
    4b2f:	48 83 c4 28          	add    $0x28,%rsp
    4b33:	5b                   	pop    %rbx
    4b34:	5d                   	pop    %rbp
    4b35:	41 5c                	pop    %r12
    4b37:	41 5d                	pop    %r13
    4b39:	41 5e                	pop    %r14
    4b3b:	41 5f                	pop    %r15
    4b3d:	c3                   	retq   
    4b3e:	66 90                	xchg   %ax,%ax
    4b40:	4c 8b 7b 20          	mov    0x20(%rbx),%r15
    4b44:	4c 8b 73 18          	mov    0x18(%rbx),%r14
    4b48:	ba 05 00 00 00       	mov    $0x5,%edx
    4b4d:	31 ff                	xor    %edi,%edi
    4b4f:	4c 8b 6b 10          	mov    0x10(%rbx),%r13
    4b53:	4c 8b 63 08          	mov    0x8(%rbx),%r12
    4b57:	48 8d 35 1a 20 00 00 	lea    0x201a(%rip),%rsi        # 6b78 <__progname@@GLIBC_2.2.5-0x2508>
    4b5e:	48 8b 1b             	mov    (%rbx),%rbx
    4b61:	ff 15 71 43 00 00    	callq  *0x4371(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4b67:	41 57                	push   %r15
    4b69:	eb a4                	jmp    4b0f <__progname@@GLIBC_2.2.5-0x4571>
    4b6b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    4b70:	4c 8b 43 08          	mov    0x8(%rbx),%r8
    4b74:	4c 8b 63 28          	mov    0x28(%rbx),%r12
    4b78:	ba 05 00 00 00       	mov    $0x5,%edx
    4b7d:	31 ff                	xor    %edi,%edi
    4b7f:	4c 8b 7b 20          	mov    0x20(%rbx),%r15
    4b83:	4c 8b 73 18          	mov    0x18(%rbx),%r14
    4b87:	48 8d 35 12 20 00 00 	lea    0x2012(%rip),%rsi        # 6ba0 <__progname@@GLIBC_2.2.5-0x24e0>
    4b8e:	4c 89 04 24          	mov    %r8,(%rsp)
    4b92:	4c 8b 6b 10          	mov    0x10(%rbx),%r13
    4b96:	48 8b 1b             	mov    (%rbx),%rbx
    4b99:	ff 15 39 43 00 00    	callq  *0x4339(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4b9f:	48 83 ec 08          	sub    $0x8,%rsp
    4ba3:	4d 89 e9             	mov    %r13,%r9
    4ba6:	41 54                	push   %r12
    4ba8:	41 57                	push   %r15
    4baa:	41 56                	push   %r14
    4bac:	4c 8b 44 24 20       	mov    0x20(%rsp),%r8
    4bb1:	48 89 d9             	mov    %rbx,%rcx
    4bb4:	48 89 c2             	mov    %rax,%rdx
    4bb7:	48 89 ef             	mov    %rbp,%rdi
    4bba:	be 01 00 00 00       	mov    $0x1,%esi
    4bbf:	31 c0                	xor    %eax,%eax
    4bc1:	ff 15 f1 43 00 00    	callq  *0x43f1(%rip)        # 8fb8 <__fprintf_chk@GLIBC_2.3.4>
    4bc7:	48 83 c4 20          	add    $0x20,%rsp
    4bcb:	48 83 c4 28          	add    $0x28,%rsp
    4bcf:	5b                   	pop    %rbx
    4bd0:	5d                   	pop    %rbp
    4bd1:	41 5c                	pop    %r12
    4bd3:	41 5d                	pop    %r13
    4bd5:	41 5e                	pop    %r14
    4bd7:	41 5f                	pop    %r15
    4bd9:	c3                   	retq   
    4bda:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    4be0:	4c 8b 4b 10          	mov    0x10(%rbx),%r9
    4be4:	4c 8b 6b 30          	mov    0x30(%rbx),%r13
    4be8:	ba 05 00 00 00       	mov    $0x5,%edx
    4bed:	31 ff                	xor    %edi,%edi
    4bef:	4c 8b 63 28          	mov    0x28(%rbx),%r12
    4bf3:	4c 8b 7b 20          	mov    0x20(%rbx),%r15
    4bf7:	48 8d 35 ca 1f 00 00 	lea    0x1fca(%rip),%rsi        # 6bc8 <__progname@@GLIBC_2.2.5-0x24b8>
    4bfe:	4c 8b 73 18          	mov    0x18(%rbx),%r14
    4c02:	4c 8b 43 08          	mov    0x8(%rbx),%r8
    4c06:	4c 89 4c 24 08       	mov    %r9,0x8(%rsp)
    4c0b:	48 8b 1b             	mov    (%rbx),%rbx
    4c0e:	4c 89 04 24          	mov    %r8,(%rsp)
    4c12:	ff 15 c0 42 00 00    	callq  *0x42c0(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4c18:	41 55                	push   %r13
    4c1a:	41 54                	push   %r12
    4c1c:	41 57                	push   %r15
    4c1e:	41 56                	push   %r14
    4c20:	4c 8b 4c 24 28       	mov    0x28(%rsp),%r9
    4c25:	eb 85                	jmp    4bac <__progname@@GLIBC_2.2.5-0x44d4>
    4c27:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    4c2e:	00 00 
    4c30:	4c 8b 53 40          	mov    0x40(%rbx),%r10
    4c34:	4c 8b 4b 38          	mov    0x38(%rbx),%r9
    4c38:	ba 05 00 00 00       	mov    $0x5,%edx
    4c3d:	48 8d 35 1c 20 00 00 	lea    0x201c(%rip),%rsi        # 6c60 <__progname@@GLIBC_2.2.5-0x2420>
    4c44:	48 8b 43 10          	mov    0x10(%rbx),%rax
    4c48:	4c 8b 43 08          	mov    0x8(%rbx),%r8
    4c4c:	4c 8b 6b 30          	mov    0x30(%rbx),%r13
    4c50:	4c 8b 63 28          	mov    0x28(%rbx),%r12
    4c54:	4c 89 54 24 18       	mov    %r10,0x18(%rsp)
    4c59:	4c 8b 7b 20          	mov    0x20(%rbx),%r15
    4c5d:	4c 8b 73 18          	mov    0x18(%rbx),%r14
    4c61:	4c 89 4c 24 10       	mov    %r9,0x10(%rsp)
    4c66:	48 89 04 24          	mov    %rax,(%rsp)
    4c6a:	48 8b 1b             	mov    (%rbx),%rbx
    4c6d:	4c 89 44 24 08       	mov    %r8,0x8(%rsp)
    4c72:	e9 7b fd ff ff       	jmpq   49f2 <__progname@@GLIBC_2.2.5-0x468e>
    4c77:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    4c7e:	00 00 
    4c80:	45 31 c9             	xor    %r9d,%r9d
    4c83:	49 83 38 00          	cmpq   $0x0,(%r8)
    4c87:	74 12                	je     4c9b <__progname@@GLIBC_2.2.5-0x43e5>
    4c89:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    4c90:	49 83 c1 01          	add    $0x1,%r9
    4c94:	4b 83 3c c8 00       	cmpq   $0x0,(%r8,%r9,8)
    4c99:	75 f5                	jne    4c90 <__progname@@GLIBC_2.2.5-0x43f0>
    4c9b:	e9 b0 fb ff ff       	jmpq   4850 <__progname@@GLIBC_2.2.5-0x4830>
    4ca0:	48 83 ec 68          	sub    $0x68,%rsp
    4ca4:	45 31 c9             	xor    %r9d,%r9d
    4ca7:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    4cae:	00 00 
    4cb0:	48 89 44 24 58       	mov    %rax,0x58(%rsp)
    4cb5:	31 c0                	xor    %eax,%eax
    4cb7:	49 89 e3             	mov    %rsp,%r11
    4cba:	eb 27                	jmp    4ce3 <__progname@@GLIBC_2.2.5-0x439d>
    4cbc:	0f 1f 40 00          	nopl   0x0(%rax)
    4cc0:	41 89 c2             	mov    %eax,%r10d
    4cc3:	83 c0 08             	add    $0x8,%eax
    4cc6:	4d 03 50 10          	add    0x10(%r8),%r10
    4cca:	41 89 00             	mov    %eax,(%r8)
    4ccd:	49 8b 02             	mov    (%r10),%rax
    4cd0:	4b 89 04 cb          	mov    %rax,(%r11,%r9,8)
    4cd4:	48 85 c0             	test   %rax,%rax
    4cd7:	74 2f                	je     4d08 <__progname@@GLIBC_2.2.5-0x4378>
    4cd9:	49 83 c1 01          	add    $0x1,%r9
    4cdd:	49 83 f9 0a          	cmp    $0xa,%r9
    4ce1:	74 25                	je     4d08 <__progname@@GLIBC_2.2.5-0x4378>
    4ce3:	41 8b 00             	mov    (%r8),%eax
    4ce6:	83 f8 2f             	cmp    $0x2f,%eax
    4ce9:	76 d5                	jbe    4cc0 <__progname@@GLIBC_2.2.5-0x43c0>
    4ceb:	4d 8b 50 08          	mov    0x8(%r8),%r10
    4cef:	49 8d 42 08          	lea    0x8(%r10),%rax
    4cf3:	49 89 40 08          	mov    %rax,0x8(%r8)
    4cf7:	49 8b 02             	mov    (%r10),%rax
    4cfa:	4b 89 04 cb          	mov    %rax,(%r11,%r9,8)
    4cfe:	48 85 c0             	test   %rax,%rax
    4d01:	75 d6                	jne    4cd9 <__progname@@GLIBC_2.2.5-0x43a7>
    4d03:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    4d08:	4d 89 d8             	mov    %r11,%r8
    4d0b:	e8 40 fb ff ff       	callq  4850 <__progname@@GLIBC_2.2.5-0x4830>
    4d10:	48 8b 44 24 58       	mov    0x58(%rsp),%rax
    4d15:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    4d1c:	00 00 
    4d1e:	75 05                	jne    4d25 <__progname@@GLIBC_2.2.5-0x435b>
    4d20:	48 83 c4 68          	add    $0x68,%rsp
    4d24:	c3                   	retq   
    4d25:	ff 15 c5 41 00 00    	callq  *0x41c5(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    4d2b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    4d30:	55                   	push   %rbp
    4d31:	41 ba 20 00 00 00    	mov    $0x20,%r10d
    4d37:	53                   	push   %rbx
    4d38:	31 db                	xor    %ebx,%ebx
    4d3a:	48 81 ec b8 00 00 00 	sub    $0xb8,%rsp
    4d41:	4c 89 84 24 a0 00 00 	mov    %r8,0xa0(%rsp)
    4d48:	00 
    4d49:	4c 8d 9c 24 d0 00 00 	lea    0xd0(%rsp),%r11
    4d50:	00 
    4d51:	4c 8d 44 24 20       	lea    0x20(%rsp),%r8
    4d56:	4c 89 8c 24 a8 00 00 	mov    %r9,0xa8(%rsp)
    4d5d:	00 
    4d5e:	45 31 c9             	xor    %r9d,%r9d
    4d61:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    4d68:	00 00 
    4d6a:	48 89 44 24 78       	mov    %rax,0x78(%rsp)
    4d6f:	31 c0                	xor    %eax,%eax
    4d71:	48 8d 84 24 d0 00 00 	lea    0xd0(%rsp),%rax
    4d78:	00 
    4d79:	c7 44 24 08 20 00 00 	movl   $0x20,0x8(%rsp)
    4d80:	00 
    4d81:	48 89 44 24 10       	mov    %rax,0x10(%rsp)
    4d86:	48 8d 84 24 80 00 00 	lea    0x80(%rsp),%rax
    4d8d:	00 
    4d8e:	48 89 44 24 18       	mov    %rax,0x18(%rsp)
    4d93:	48 89 c5             	mov    %rax,%rbp
    4d96:	eb 2d                	jmp    4dc5 <__progname@@GLIBC_2.2.5-0x42bb>
    4d98:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    4d9f:	00 
    4da0:	44 89 d0             	mov    %r10d,%eax
    4da3:	bb 01 00 00 00       	mov    $0x1,%ebx
    4da8:	41 83 c2 08          	add    $0x8,%r10d
    4dac:	48 01 e8             	add    %rbp,%rax
    4daf:	48 8b 00             	mov    (%rax),%rax
    4db2:	4b 89 04 c8          	mov    %rax,(%r8,%r9,8)
    4db6:	48 85 c0             	test   %rax,%rax
    4db9:	74 25                	je     4de0 <__progname@@GLIBC_2.2.5-0x42a0>
    4dbb:	49 83 c1 01          	add    $0x1,%r9
    4dbf:	49 83 f9 0a          	cmp    $0xa,%r9
    4dc3:	74 1b                	je     4de0 <__progname@@GLIBC_2.2.5-0x42a0>
    4dc5:	41 83 fa 2f          	cmp    $0x2f,%r10d
    4dc9:	76 d5                	jbe    4da0 <__progname@@GLIBC_2.2.5-0x42e0>
    4dcb:	4c 89 d8             	mov    %r11,%rax
    4dce:	49 83 c3 08          	add    $0x8,%r11
    4dd2:	48 8b 00             	mov    (%rax),%rax
    4dd5:	4b 89 04 c8          	mov    %rax,(%r8,%r9,8)
    4dd9:	48 85 c0             	test   %rax,%rax
    4ddc:	75 dd                	jne    4dbb <__progname@@GLIBC_2.2.5-0x42c5>
    4dde:	66 90                	xchg   %ax,%ax
    4de0:	84 db                	test   %bl,%bl
    4de2:	74 05                	je     4de9 <__progname@@GLIBC_2.2.5-0x4297>
    4de4:	44 89 54 24 08       	mov    %r10d,0x8(%rsp)
    4de9:	e8 62 fa ff ff       	callq  4850 <__progname@@GLIBC_2.2.5-0x4830>
    4dee:	48 8b 44 24 78       	mov    0x78(%rsp),%rax
    4df3:	64 48 33 04 25 28 00 	xor    %fs:0x28,%rax
    4dfa:	00 00 
    4dfc:	75 0a                	jne    4e08 <__progname@@GLIBC_2.2.5-0x4278>
    4dfe:	48 81 c4 b8 00 00 00 	add    $0xb8,%rsp
    4e05:	5b                   	pop    %rbx
    4e06:	5d                   	pop    %rbp
    4e07:	c3                   	retq   
    4e08:	ff 15 e2 40 00 00    	callq  *0x40e2(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    4e0e:	66 90                	xchg   %ax,%ax
    4e10:	53                   	push   %rbx
    4e11:	ba 05 00 00 00       	mov    $0x5,%edx
    4e16:	48 8d 35 25 1c 00 00 	lea    0x1c25(%rip),%rsi        # 6a42 <__progname@@GLIBC_2.2.5-0x263e>
    4e1d:	31 ff                	xor    %edi,%edi
    4e1f:	ff 15 b3 40 00 00    	callq  *0x40b3(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4e25:	48 8d 15 2b 1c 00 00 	lea    0x1c2b(%rip),%rdx        # 6a57 <__progname@@GLIBC_2.2.5-0x2629>
    4e2c:	bf 01 00 00 00       	mov    $0x1,%edi
    4e31:	48 89 c6             	mov    %rax,%rsi
    4e34:	31 c0                	xor    %eax,%eax
    4e36:	ff 15 4c 41 00 00    	callq  *0x414c(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    4e3c:	ba 05 00 00 00       	mov    $0x5,%edx
    4e41:	48 8d 35 25 1c 00 00 	lea    0x1c25(%rip),%rsi        # 6a6d <__progname@@GLIBC_2.2.5-0x2613>
    4e48:	31 ff                	xor    %edi,%edi
    4e4a:	ff 15 88 40 00 00    	callq  *0x4088(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4e50:	48 8d 0d 71 13 00 00 	lea    0x1371(%rip),%rcx        # 61c8 <__progname@@GLIBC_2.2.5-0x2eb8>
    4e57:	bf 01 00 00 00       	mov    $0x1,%edi
    4e5c:	48 8d 15 1b 12 00 00 	lea    0x121b(%rip),%rdx        # 607e <__progname@@GLIBC_2.2.5-0x3002>
    4e63:	48 89 c6             	mov    %rax,%rsi
    4e66:	31 c0                	xor    %eax,%eax
    4e68:	ff 15 1a 41 00 00    	callq  *0x411a(%rip)        # 8f88 <__printf_chk@GLIBC_2.3.4>
    4e6e:	48 8b 1d 13 42 00 00 	mov    0x4213(%rip),%rbx        # 9088 <stdout@@GLIBC_2.2.5>
    4e75:	31 ff                	xor    %edi,%edi
    4e77:	48 8d 35 22 1e 00 00 	lea    0x1e22(%rip),%rsi        # 6ca0 <__progname@@GLIBC_2.2.5-0x23e0>
    4e7e:	ba 05 00 00 00       	mov    $0x5,%edx
    4e83:	ff 15 4f 40 00 00    	callq  *0x404f(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    4e89:	48 89 de             	mov    %rbx,%rsi
    4e8c:	5b                   	pop    %rbx
    4e8d:	48 89 c7             	mov    %rax,%rdi
    4e90:	ff 25 9a 40 00 00    	jmpq   *0x409a(%rip)        # 8f30 <fputs_unlocked@GLIBC_2.2.5>
    4e96:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    4e9d:	00 00 00 
    4ea0:	53                   	push   %rbx
    4ea1:	48 89 fb             	mov    %rdi,%rbx
    4ea4:	ff 15 ae 40 00 00    	callq  *0x40ae(%rip)        # 8f58 <malloc@GLIBC_2.2.5>
    4eaa:	48 85 c0             	test   %rax,%rax
    4ead:	75 05                	jne    4eb4 <__progname@@GLIBC_2.2.5-0x41cc>
    4eaf:	48 85 db             	test   %rbx,%rbx
    4eb2:	75 02                	jne    4eb6 <__progname@@GLIBC_2.2.5-0x41ca>
    4eb4:	5b                   	pop    %rbx
    4eb5:	c3                   	retq   
    4eb6:	67 e8 44 02 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    4ebc:	0f 1f 40 00          	nopl   0x0(%rax)
    4ec0:	48 89 f8             	mov    %rdi,%rax
    4ec3:	48 f7 e6             	mul    %rsi
    4ec6:	48 89 c7             	mov    %rax,%rdi
    4ec9:	0f 90 c0             	seto   %al
    4ecc:	48 85 ff             	test   %rdi,%rdi
    4ecf:	78 0a                	js     4edb <__progname@@GLIBC_2.2.5-0x41a5>
    4ed1:	0f b6 c0             	movzbl %al,%eax
    4ed4:	48 85 c0             	test   %rax,%rax
    4ed7:	75 02                	jne    4edb <__progname@@GLIBC_2.2.5-0x41a5>
    4ed9:	eb c5                	jmp    4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    4edb:	50                   	push   %rax
    4edc:	67 e8 1e 02 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    4ee2:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    4ee9:	00 00 00 00 
    4eed:	0f 1f 00             	nopl   (%rax)
    4ef0:	eb ae                	jmp    4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    4ef2:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    4ef9:	00 00 00 00 
    4efd:	0f 1f 00             	nopl   (%rax)
    4f00:	53                   	push   %rbx
    4f01:	48 89 f3             	mov    %rsi,%rbx
    4f04:	48 85 f6             	test   %rsi,%rsi
    4f07:	75 05                	jne    4f0e <__progname@@GLIBC_2.2.5-0x4172>
    4f09:	48 85 ff             	test   %rdi,%rdi
    4f0c:	75 1a                	jne    4f28 <__progname@@GLIBC_2.2.5-0x4158>
    4f0e:	48 89 de             	mov    %rbx,%rsi
    4f11:	ff 15 61 40 00 00    	callq  *0x4061(%rip)        # 8f78 <realloc@GLIBC_2.2.5>
    4f17:	48 85 c0             	test   %rax,%rax
    4f1a:	75 05                	jne    4f21 <__progname@@GLIBC_2.2.5-0x415f>
    4f1c:	48 85 db             	test   %rbx,%rbx
    4f1f:	75 11                	jne    4f32 <__progname@@GLIBC_2.2.5-0x414e>
    4f21:	5b                   	pop    %rbx
    4f22:	c3                   	retq   
    4f23:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    4f28:	ff 15 52 3f 00 00    	callq  *0x3f52(%rip)        # 8e80 <free@GLIBC_2.2.5>
    4f2e:	31 c0                	xor    %eax,%eax
    4f30:	5b                   	pop    %rbx
    4f31:	c3                   	retq   
    4f32:	67 e8 c8 01 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    4f38:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    4f3f:	00 
    4f40:	48 89 f0             	mov    %rsi,%rax
    4f43:	48 f7 e2             	mul    %rdx
    4f46:	48 89 c6             	mov    %rax,%rsi
    4f49:	0f 90 c0             	seto   %al
    4f4c:	48 85 f6             	test   %rsi,%rsi
    4f4f:	78 0a                	js     4f5b <__progname@@GLIBC_2.2.5-0x4125>
    4f51:	0f b6 c0             	movzbl %al,%eax
    4f54:	48 85 c0             	test   %rax,%rax
    4f57:	75 02                	jne    4f5b <__progname@@GLIBC_2.2.5-0x4125>
    4f59:	eb a5                	jmp    4f00 <__progname@@GLIBC_2.2.5-0x4180>
    4f5b:	50                   	push   %rax
    4f5c:	67 e8 9e 01 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    4f62:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    4f69:	00 00 00 00 
    4f6d:	0f 1f 00             	nopl   (%rax)
    4f70:	49 89 d1             	mov    %rdx,%r9
    4f73:	48 8b 0e             	mov    (%rsi),%rcx
    4f76:	48 85 ff             	test   %rdi,%rdi
    4f79:	74 35                	je     4fb0 <__progname@@GLIBC_2.2.5-0x40d0>
    4f7b:	48 b8 54 55 55 55 55 	movabs $0x5555555555555554,%rax
    4f82:	55 55 55 
    4f85:	31 d2                	xor    %edx,%edx
    4f87:	49 f7 f1             	div    %r9
    4f8a:	48 39 c8             	cmp    %rcx,%rax
    4f8d:	76 3c                	jbe    4fcb <__progname@@GLIBC_2.2.5-0x40b5>
    4f8f:	48 89 c8             	mov    %rcx,%rax
    4f92:	48 d1 e8             	shr    %rax
    4f95:	48 8d 4c 08 01       	lea    0x1(%rax,%rcx,1),%rcx
    4f9a:	48 89 0e             	mov    %rcx,(%rsi)
    4f9d:	49 0f af c9          	imul   %r9,%rcx
    4fa1:	48 89 ce             	mov    %rcx,%rsi
    4fa4:	e9 57 ff ff ff       	jmpq   4f00 <__progname@@GLIBC_2.2.5-0x4180>
    4fa9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    4fb0:	48 85 c9             	test   %rcx,%rcx
    4fb3:	74 23                	je     4fd8 <__progname@@GLIBC_2.2.5-0x40a8>
    4fb5:	48 89 c8             	mov    %rcx,%rax
    4fb8:	49 f7 e1             	mul    %r9
    4fbb:	0f 90 c2             	seto   %dl
    4fbe:	0f b6 d2             	movzbl %dl,%edx
    4fc1:	48 85 c0             	test   %rax,%rax
    4fc4:	78 05                	js     4fcb <__progname@@GLIBC_2.2.5-0x40b5>
    4fc6:	48 85 d2             	test   %rdx,%rdx
    4fc9:	74 cf                	je     4f9a <__progname@@GLIBC_2.2.5-0x40e6>
    4fcb:	50                   	push   %rax
    4fcc:	67 e8 2e 01 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    4fd2:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    4fd8:	31 d2                	xor    %edx,%edx
    4fda:	b8 80 00 00 00       	mov    $0x80,%eax
    4fdf:	45 31 c0             	xor    %r8d,%r8d
    4fe2:	49 f7 f1             	div    %r9
    4fe5:	49 81 f9 80 00 00 00 	cmp    $0x80,%r9
    4fec:	41 0f 97 c0          	seta   %r8b
    4ff0:	49 8d 0c 00          	lea    (%r8,%rax,1),%rcx
    4ff4:	eb bf                	jmp    4fb5 <__progname@@GLIBC_2.2.5-0x40cb>
    4ff6:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    4ffd:	00 00 00 
    5000:	48 8b 06             	mov    (%rsi),%rax
    5003:	48 85 ff             	test   %rdi,%rdi
    5006:	74 28                	je     5030 <__progname@@GLIBC_2.2.5-0x4050>
    5008:	48 ba 53 55 55 55 55 	movabs $0x5555555555555553,%rdx
    500f:	55 55 55 
    5012:	48 39 d0             	cmp    %rdx,%rax
    5015:	77 33                	ja     504a <__progname@@GLIBC_2.2.5-0x4036>
    5017:	48 89 c2             	mov    %rax,%rdx
    501a:	48 d1 ea             	shr    %rdx
    501d:	48 8d 44 02 01       	lea    0x1(%rdx,%rax,1),%rax
    5022:	48 89 06             	mov    %rax,(%rsi)
    5025:	48 89 c6             	mov    %rax,%rsi
    5028:	e9 d3 fe ff ff       	jmpq   4f00 <__progname@@GLIBC_2.2.5-0x4180>
    502d:	0f 1f 00             	nopl   (%rax)
    5030:	48 85 c0             	test   %rax,%rax
    5033:	75 13                	jne    5048 <__progname@@GLIBC_2.2.5-0x4038>
    5035:	b8 80 00 00 00       	mov    $0x80,%eax
    503a:	48 89 06             	mov    %rax,(%rsi)
    503d:	48 89 c6             	mov    %rax,%rsi
    5040:	e9 bb fe ff ff       	jmpq   4f00 <__progname@@GLIBC_2.2.5-0x4180>
    5045:	0f 1f 00             	nopl   (%rax)
    5048:	79 d8                	jns    5022 <__progname@@GLIBC_2.2.5-0x405e>
    504a:	50                   	push   %rax
    504b:	67 e8 af 00 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    5051:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    5058:	00 00 00 00 
    505c:	0f 1f 40 00          	nopl   0x0(%rax)
    5060:	53                   	push   %rbx
    5061:	48 89 fb             	mov    %rdi,%rbx
    5064:	e8 37 fe ff ff       	callq  4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    5069:	48 89 da             	mov    %rbx,%rdx
    506c:	31 f6                	xor    %esi,%esi
    506e:	5b                   	pop    %rbx
    506f:	48 89 c7             	mov    %rax,%rdi
    5072:	ff 25 a0 3e 00 00    	jmpq   *0x3ea0(%rip)        # 8f18 <memset@GLIBC_2.2.5>
    5078:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    507f:	00 
    5080:	48 89 f8             	mov    %rdi,%rax
    5083:	48 83 ec 08          	sub    $0x8,%rsp
    5087:	48 f7 e6             	mul    %rsi
    508a:	0f 90 c2             	seto   %dl
    508d:	48 85 c0             	test   %rax,%rax
    5090:	78 18                	js     50aa <__progname@@GLIBC_2.2.5-0x3fd6>
    5092:	0f b6 d2             	movzbl %dl,%edx
    5095:	48 85 d2             	test   %rdx,%rdx
    5098:	75 10                	jne    50aa <__progname@@GLIBC_2.2.5-0x3fd6>
    509a:	ff 15 98 3e 00 00    	callq  *0x3e98(%rip)        # 8f38 <calloc@GLIBC_2.2.5>
    50a0:	48 85 c0             	test   %rax,%rax
    50a3:	74 05                	je     50aa <__progname@@GLIBC_2.2.5-0x3fd6>
    50a5:	48 83 c4 08          	add    $0x8,%rsp
    50a9:	c3                   	retq   
    50aa:	67 e8 50 00 00 00    	addr32 callq 5100 <__progname@@GLIBC_2.2.5-0x3f80>
    50b0:	55                   	push   %rbp
    50b1:	48 89 fd             	mov    %rdi,%rbp
    50b4:	48 89 f7             	mov    %rsi,%rdi
    50b7:	53                   	push   %rbx
    50b8:	48 89 f3             	mov    %rsi,%rbx
    50bb:	48 83 ec 08          	sub    $0x8,%rsp
    50bf:	e8 dc fd ff ff       	callq  4ea0 <__progname@@GLIBC_2.2.5-0x41e0>
    50c4:	48 83 c4 08          	add    $0x8,%rsp
    50c8:	48 89 da             	mov    %rbx,%rdx
    50cb:	48 89 ee             	mov    %rbp,%rsi
    50ce:	5b                   	pop    %rbx
    50cf:	48 89 c7             	mov    %rax,%rdi
    50d2:	5d                   	pop    %rbp
    50d3:	ff 25 6f 3e 00 00    	jmpq   *0x3e6f(%rip)        # 8f48 <memcpy@GLIBC_2.14>
    50d9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    50e0:	53                   	push   %rbx
    50e1:	48 89 fb             	mov    %rdi,%rbx
    50e4:	ff 15 fe 3d 00 00    	callq  *0x3dfe(%rip)        # 8ee8 <strlen@GLIBC_2.2.5>
    50ea:	48 89 df             	mov    %rbx,%rdi
    50ed:	5b                   	pop    %rbx
    50ee:	48 8d 70 01          	lea    0x1(%rax),%rsi
    50f2:	eb bc                	jmp    50b0 <__progname@@GLIBC_2.2.5-0x3fd0>
    50f4:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    50fb:	00 00 00 
    50fe:	66 90                	xchg   %ax,%ax
    5100:	48 83 ec 08          	sub    $0x8,%rsp
    5104:	ba 05 00 00 00       	mov    $0x5,%edx
    5109:	48 8d 35 3f 1c 00 00 	lea    0x1c3f(%rip),%rsi        # 6d4f <__progname@@GLIBC_2.2.5-0x2331>
    5110:	31 ff                	xor    %edi,%edi
    5112:	ff 15 c0 3d 00 00    	callq  *0x3dc0(%rip)        # 8ed8 <dcgettext@GLIBC_2.2.5>
    5118:	8b 3d fa 3e 00 00    	mov    0x3efa(%rip),%edi        # 9018 <__progname@@GLIBC_2.2.5-0x68>
    511e:	48 8d 15 b0 11 00 00 	lea    0x11b0(%rip),%rdx        # 62d5 <__progname@@GLIBC_2.2.5-0x2dab>
    5125:	31 f6                	xor    %esi,%esi
    5127:	48 89 c1             	mov    %rax,%rcx
    512a:	31 c0                	xor    %eax,%eax
    512c:	ff 15 5e 3e 00 00    	callq  *0x3e5e(%rip)        # 8f90 <error@GLIBC_2.2.5>
    5132:	ff 15 50 3d 00 00    	callq  *0x3d50(%rip)        # 8e88 <abort@GLIBC_2.2.5>
    5138:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    513f:	00 
    5140:	41 55                	push   %r13
    5142:	49 89 f5             	mov    %rsi,%r13
    5145:	41 54                	push   %r12
    5147:	49 89 d4             	mov    %rdx,%r12
    514a:	55                   	push   %rbp
    514b:	53                   	push   %rbx
    514c:	48 89 fb             	mov    %rdi,%rbx
    514f:	48 83 ec 18          	sub    $0x18,%rsp
    5153:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    515a:	00 00 
    515c:	48 89 44 24 08       	mov    %rax,0x8(%rsp)
    5161:	31 c0                	xor    %eax,%eax
    5163:	48 85 ff             	test   %rdi,%rdi
    5166:	48 8d 44 24 04       	lea    0x4(%rsp),%rax
    516b:	48 0f 44 d8          	cmove  %rax,%rbx
    516f:	48 89 df             	mov    %rbx,%rdi
    5172:	ff 15 88 3d 00 00    	callq  *0x3d88(%rip)        # 8f00 <mbrtowc@GLIBC_2.2.5>
    5178:	48 89 c5             	mov    %rax,%rbp
    517b:	48 83 f8 fd          	cmp    $0xfffffffffffffffd,%rax
    517f:	76 05                	jbe    5186 <__progname@@GLIBC_2.2.5-0x3efa>
    5181:	4d 85 e4             	test   %r12,%r12
    5184:	75 22                	jne    51a8 <__progname@@GLIBC_2.2.5-0x3ed8>
    5186:	48 8b 54 24 08       	mov    0x8(%rsp),%rdx
    518b:	64 48 33 14 25 28 00 	xor    %fs:0x28,%rdx
    5192:	00 00 
    5194:	48 89 e8             	mov    %rbp,%rax
    5197:	75 29                	jne    51c2 <__progname@@GLIBC_2.2.5-0x3ebe>
    5199:	48 83 c4 18          	add    $0x18,%rsp
    519d:	5b                   	pop    %rbx
    519e:	5d                   	pop    %rbp
    519f:	41 5c                	pop    %r12
    51a1:	41 5d                	pop    %r13
    51a3:	c3                   	retq   
    51a4:	0f 1f 40 00          	nopl   0x0(%rax)
    51a8:	31 ff                	xor    %edi,%edi
    51aa:	67 e8 90 00 00 00    	addr32 callq 5240 <__progname@@GLIBC_2.2.5-0x3e40>
    51b0:	84 c0                	test   %al,%al
    51b2:	75 d2                	jne    5186 <__progname@@GLIBC_2.2.5-0x3efa>
    51b4:	41 0f b6 45 00       	movzbl 0x0(%r13),%eax
    51b9:	bd 01 00 00 00       	mov    $0x1,%ebp
    51be:	89 03                	mov    %eax,(%rbx)
    51c0:	eb c4                	jmp    5186 <__progname@@GLIBC_2.2.5-0x3efa>
    51c2:	ff 15 28 3d 00 00    	callq  *0x3d28(%rip)        # 8ef0 <__stack_chk_fail@GLIBC_2.4>
    51c8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    51cf:	00 
    51d0:	41 54                	push   %r12
    51d2:	55                   	push   %rbp
    51d3:	48 89 fd             	mov    %rdi,%rbp
    51d6:	53                   	push   %rbx
    51d7:	ff 15 d3 3c 00 00    	callq  *0x3cd3(%rip)        # 8eb0 <__fpending@GLIBC_2.2.5>
    51dd:	8b 5d 00             	mov    0x0(%rbp),%ebx
    51e0:	48 89 ef             	mov    %rbp,%rdi
    51e3:	49 89 c4             	mov    %rax,%r12
    51e6:	83 e3 20             	and    $0x20,%ebx
    51e9:	67 e8 f1 00 00 00    	addr32 callq 52e0 <__progname@@GLIBC_2.2.5-0x3da0>
    51ef:	85 db                	test   %ebx,%ebx
    51f1:	75 25                	jne    5218 <__progname@@GLIBC_2.2.5-0x3e68>
    51f3:	85 c0                	test   %eax,%eax
    51f5:	74 16                	je     520d <__progname@@GLIBC_2.2.5-0x3e73>
    51f7:	4d 85 e4             	test   %r12,%r12
    51fa:	75 33                	jne    522f <__progname@@GLIBC_2.2.5-0x3e51>
    51fc:	ff 15 8e 3c 00 00    	callq  *0x3c8e(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    5202:	83 38 09             	cmpl   $0x9,(%rax)
    5205:	0f 95 c0             	setne  %al
    5208:	0f b6 c0             	movzbl %al,%eax
    520b:	f7 d8                	neg    %eax
    520d:	5b                   	pop    %rbx
    520e:	5d                   	pop    %rbp
    520f:	41 5c                	pop    %r12
    5211:	c3                   	retq   
    5212:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    5218:	85 c0                	test   %eax,%eax
    521a:	75 13                	jne    522f <__progname@@GLIBC_2.2.5-0x3e51>
    521c:	ff 15 6e 3c 00 00    	callq  *0x3c6e(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    5222:	c7 00 00 00 00 00    	movl   $0x0,(%rax)
    5228:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    522d:	eb de                	jmp    520d <__progname@@GLIBC_2.2.5-0x3e73>
    522f:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    5234:	eb d7                	jmp    520d <__progname@@GLIBC_2.2.5-0x3e73>
    5236:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    523d:	00 00 00 
    5240:	48 83 ec 08          	sub    $0x8,%rsp
    5244:	31 f6                	xor    %esi,%esi
    5246:	ff 15 34 3d 00 00    	callq  *0x3d34(%rip)        # 8f80 <setlocale@GLIBC_2.2.5>
    524c:	48 89 c2             	mov    %rax,%rdx
    524f:	b8 01 00 00 00       	mov    $0x1,%eax
    5254:	48 85 d2             	test   %rdx,%rdx
    5257:	74 1d                	je     5276 <__progname@@GLIBC_2.2.5-0x3e0a>
    5259:	b9 02 00 00 00       	mov    $0x2,%ecx
    525e:	48 8d 3d fb 1a 00 00 	lea    0x1afb(%rip),%rdi        # 6d60 <__progname@@GLIBC_2.2.5-0x2320>
    5265:	48 89 d6             	mov    %rdx,%rsi
    5268:	f3 a6                	repz cmpsb %es:(%rdi),%ds:(%rsi)
    526a:	0f 97 c1             	seta   %cl
    526d:	80 d9 00             	sbb    $0x0,%cl
    5270:	31 c0                	xor    %eax,%eax
    5272:	84 c9                	test   %cl,%cl
    5274:	75 0a                	jne    5280 <__progname@@GLIBC_2.2.5-0x3e00>
    5276:	48 83 c4 08          	add    $0x8,%rsp
    527a:	c3                   	retq   
    527b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    5280:	b9 06 00 00 00       	mov    $0x6,%ecx
    5285:	48 8d 3d d6 1a 00 00 	lea    0x1ad6(%rip),%rdi        # 6d62 <__progname@@GLIBC_2.2.5-0x231e>
    528c:	48 89 d6             	mov    %rdx,%rsi
    528f:	f3 a6                	repz cmpsb %es:(%rdi),%ds:(%rsi)
    5291:	0f 97 c0             	seta   %al
    5294:	1c 00                	sbb    $0x0,%al
    5296:	84 c0                	test   %al,%al
    5298:	0f 95 c0             	setne  %al
    529b:	48 83 c4 08          	add    $0x8,%rsp
    529f:	c3                   	retq   
    52a0:	48 83 ec 08          	sub    $0x8,%rsp
    52a4:	bf 0e 00 00 00       	mov    $0xe,%edi
    52a9:	ff 15 b9 3c 00 00    	callq  *0x3cb9(%rip)        # 8f68 <nl_langinfo@GLIBC_2.2.5>
    52af:	48 85 c0             	test   %rax,%rax
    52b2:	74 1c                	je     52d0 <__progname@@GLIBC_2.2.5-0x3db0>
    52b4:	80 38 00             	cmpb   $0x0,(%rax)
    52b7:	48 8d 15 aa 1a 00 00 	lea    0x1aaa(%rip),%rdx        # 6d68 <__progname@@GLIBC_2.2.5-0x2318>
    52be:	48 0f 44 c2          	cmove  %rdx,%rax
    52c2:	48 83 c4 08          	add    $0x8,%rsp
    52c6:	c3                   	retq   
    52c7:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
    52ce:	00 00 
    52d0:	48 8d 05 91 1a 00 00 	lea    0x1a91(%rip),%rax        # 6d68 <__progname@@GLIBC_2.2.5-0x2318>
    52d7:	48 83 c4 08          	add    $0x8,%rsp
    52db:	c3                   	retq   
    52dc:	0f 1f 40 00          	nopl   0x0(%rax)
    52e0:	41 54                	push   %r12
    52e2:	55                   	push   %rbp
    52e3:	53                   	push   %rbx
    52e4:	48 89 fb             	mov    %rdi,%rbx
    52e7:	ff 15 63 3c 00 00    	callq  *0x3c63(%rip)        # 8f50 <fileno@GLIBC_2.2.5>
    52ed:	48 89 df             	mov    %rbx,%rdi
    52f0:	85 c0                	test   %eax,%eax
    52f2:	78 5d                	js     5351 <__progname@@GLIBC_2.2.5-0x3d2f>
    52f4:	ff 15 76 3c 00 00    	callq  *0x3c76(%rip)        # 8f70 <__freading@GLIBC_2.2.5>
    52fa:	85 c0                	test   %eax,%eax
    52fc:	75 32                	jne    5330 <__progname@@GLIBC_2.2.5-0x3d50>
    52fe:	48 89 df             	mov    %rbx,%rdi
    5301:	67 e8 69 00 00 00    	addr32 callq 5370 <__progname@@GLIBC_2.2.5-0x3d10>
    5307:	85 c0                	test   %eax,%eax
    5309:	74 43                	je     534e <__progname@@GLIBC_2.2.5-0x3d32>
    530b:	ff 15 7f 3b 00 00    	callq  *0x3b7f(%rip)        # 8e90 <__errno_location@GLIBC_2.2.5>
    5311:	48 89 df             	mov    %rbx,%rdi
    5314:	44 8b 20             	mov    (%rax),%r12d
    5317:	48 89 c5             	mov    %rax,%rbp
    531a:	ff 15 a8 3b 00 00    	callq  *0x3ba8(%rip)        # 8ec8 <fclose@GLIBC_2.2.5>
    5320:	45 85 e4             	test   %r12d,%r12d
    5323:	75 3b                	jne    5360 <__progname@@GLIBC_2.2.5-0x3d20>
    5325:	5b                   	pop    %rbx
    5326:	5d                   	pop    %rbp
    5327:	41 5c                	pop    %r12
    5329:	c3                   	retq   
    532a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    5330:	48 89 df             	mov    %rbx,%rdi
    5333:	ff 15 17 3c 00 00    	callq  *0x3c17(%rip)        # 8f50 <fileno@GLIBC_2.2.5>
    5339:	31 f6                	xor    %esi,%esi
    533b:	ba 01 00 00 00       	mov    $0x1,%edx
    5340:	89 c7                	mov    %eax,%edi
    5342:	ff 15 c8 3b 00 00    	callq  *0x3bc8(%rip)        # 8f10 <lseek@GLIBC_2.2.5>
    5348:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
    534c:	75 b0                	jne    52fe <__progname@@GLIBC_2.2.5-0x3d82>
    534e:	48 89 df             	mov    %rbx,%rdi
    5351:	5b                   	pop    %rbx
    5352:	5d                   	pop    %rbp
    5353:	41 5c                	pop    %r12
    5355:	ff 25 6d 3b 00 00    	jmpq   *0x3b6d(%rip)        # 8ec8 <fclose@GLIBC_2.2.5>
    535b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    5360:	44 89 65 00          	mov    %r12d,0x0(%rbp)
    5364:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    5369:	eb ba                	jmp    5325 <__progname@@GLIBC_2.2.5-0x3d5b>
    536b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    5370:	53                   	push   %rbx
    5371:	48 89 fb             	mov    %rdi,%rbx
    5374:	48 85 ff             	test   %rdi,%rdi
    5377:	74 12                	je     538b <__progname@@GLIBC_2.2.5-0x3cf5>
    5379:	ff 15 f1 3b 00 00    	callq  *0x3bf1(%rip)        # 8f70 <__freading@GLIBC_2.2.5>
    537f:	85 c0                	test   %eax,%eax
    5381:	74 08                	je     538b <__progname@@GLIBC_2.2.5-0x3cf5>
    5383:	f7 03 00 01 00 00    	testl  $0x100,(%rbx)
    5389:	75 0d                	jne    5398 <__progname@@GLIBC_2.2.5-0x3ce8>
    538b:	48 89 df             	mov    %rbx,%rdi
    538e:	5b                   	pop    %rbx
    538f:	ff 25 cb 3b 00 00    	jmpq   *0x3bcb(%rip)        # 8f60 <fflush@GLIBC_2.2.5>
    5395:	0f 1f 00             	nopl   (%rax)
    5398:	48 89 df             	mov    %rbx,%rdi
    539b:	ba 01 00 00 00       	mov    $0x1,%edx
    53a0:	31 f6                	xor    %esi,%esi
    53a2:	67 e8 18 00 00 00    	addr32 callq 53c0 <__progname@@GLIBC_2.2.5-0x3cc0>
    53a8:	48 89 df             	mov    %rbx,%rdi
    53ab:	5b                   	pop    %rbx
    53ac:	ff 25 ae 3b 00 00    	jmpq   *0x3bae(%rip)        # 8f60 <fflush@GLIBC_2.2.5>
    53b2:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    53b9:	00 00 00 
    53bc:	0f 1f 40 00          	nopl   0x0(%rax)
    53c0:	48 8b 47 08          	mov    0x8(%rdi),%rax
    53c4:	48 39 47 10          	cmp    %rax,0x10(%rdi)
    53c8:	74 06                	je     53d0 <__progname@@GLIBC_2.2.5-0x3cb0>
    53ca:	ff 25 c8 3b 00 00    	jmpq   *0x3bc8(%rip)        # 8f98 <fseeko@GLIBC_2.2.5>
    53d0:	48 8b 47 20          	mov    0x20(%rdi),%rax
    53d4:	48 39 47 28          	cmp    %rax,0x28(%rdi)
    53d8:	75 f0                	jne    53ca <__progname@@GLIBC_2.2.5-0x3cb6>
    53da:	48 83 7f 48 00       	cmpq   $0x0,0x48(%rdi)
    53df:	75 e9                	jne    53ca <__progname@@GLIBC_2.2.5-0x3cb6>
    53e1:	41 54                	push   %r12
    53e3:	41 89 d4             	mov    %edx,%r12d
    53e6:	55                   	push   %rbp
    53e7:	48 89 f5             	mov    %rsi,%rbp
    53ea:	53                   	push   %rbx
    53eb:	48 89 fb             	mov    %rdi,%rbx
    53ee:	ff 15 5c 3b 00 00    	callq  *0x3b5c(%rip)        # 8f50 <fileno@GLIBC_2.2.5>
    53f4:	44 89 e2             	mov    %r12d,%edx
    53f7:	48 89 ee             	mov    %rbp,%rsi
    53fa:	89 c7                	mov    %eax,%edi
    53fc:	ff 15 0e 3b 00 00    	callq  *0x3b0e(%rip)        # 8f10 <lseek@GLIBC_2.2.5>
    5402:	48 83 f8 ff          	cmp    $0xffffffffffffffff,%rax
    5406:	74 0c                	je     5414 <__progname@@GLIBC_2.2.5-0x3c6c>
    5408:	83 23 ef             	andl   $0xffffffef,(%rbx)
    540b:	48 89 83 90 00 00 00 	mov    %rax,0x90(%rbx)
    5412:	31 c0                	xor    %eax,%eax
    5414:	5b                   	pop    %rbx
    5415:	5d                   	pop    %rbp
    5416:	41 5c                	pop    %r12
    5418:	c3                   	retq   
    5419:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    5420:	f3 0f 1e fa          	endbr64 
    5424:	41 57                	push   %r15
    5426:	49 89 d7             	mov    %rdx,%r15
    5429:	41 56                	push   %r14
    542b:	49 89 f6             	mov    %rsi,%r14
    542e:	41 55                	push   %r13
    5430:	41 89 fd             	mov    %edi,%r13d
    5433:	41 54                	push   %r12
    5435:	4c 8d 25 b4 37 00 00 	lea    0x37b4(%rip),%r12        # 8bf0 <__progname@@GLIBC_2.2.5-0x490>
    543c:	55                   	push   %rbp
    543d:	48 8d 2d b4 37 00 00 	lea    0x37b4(%rip),%rbp        # 8bf8 <__progname@@GLIBC_2.2.5-0x488>
    5444:	53                   	push   %rbx
    5445:	4c 29 e5             	sub    %r12,%rbp
    5448:	48 83 ec 08          	sub    $0x8,%rsp
    544c:	67 e8 ae cb ff ff    	addr32 callq 2000 <__progname@@GLIBC_2.2.5-0x7080>
    5452:	48 c1 fd 03          	sar    $0x3,%rbp
    5456:	74 1e                	je     5476 <__progname@@GLIBC_2.2.5-0x3c0a>
    5458:	31 db                	xor    %ebx,%ebx
    545a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    5460:	4c 89 fa             	mov    %r15,%rdx
    5463:	4c 89 f6             	mov    %r14,%rsi
    5466:	44 89 ef             	mov    %r13d,%edi
    5469:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
    546d:	48 83 c3 01          	add    $0x1,%rbx
    5471:	48 39 dd             	cmp    %rbx,%rbp
    5474:	75 ea                	jne    5460 <__progname@@GLIBC_2.2.5-0x3c20>
    5476:	48 83 c4 08          	add    $0x8,%rsp
    547a:	5b                   	pop    %rbx
    547b:	5d                   	pop    %rbp
    547c:	41 5c                	pop    %r12
    547e:	41 5d                	pop    %r13
    5480:	41 5e                	pop    %r14
    5482:	41 5f                	pop    %r15
    5484:	c3                   	retq   
    5485:	66 66 2e 0f 1f 84 00 	data16 nopw %cs:0x0(%rax,%rax,1)
    548c:	00 00 00 00 
    5490:	f3 0f 1e fa          	endbr64 
    5494:	c3                   	retq   
    5495:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
    549c:	00 00 00 
    549f:	90                   	nop
    54a0:	f3 0f 1e fa          	endbr64 
    54a4:	48 8b 15 5d 3b 00 00 	mov    0x3b5d(%rip),%rdx        # 9008 <__progname@@GLIBC_2.2.5-0x78>
    54ab:	31 f6                	xor    %esi,%esi
    54ad:	ff 25 ed 3a 00 00    	jmpq   *0x3aed(%rip)        # 8fa0 <__cxa_atexit@GLIBC_2.2.5>

Disassembly of section .fini:

00000000000054b4 <.fini>:
    54b4:	f3 0f 1e fa          	endbr64 
    54b8:	48 83 ec 08          	sub    $0x8,%rsp
    54bc:	48 83 c4 08          	add    $0x8,%rsp
    54c0:	c3                   	retq   
