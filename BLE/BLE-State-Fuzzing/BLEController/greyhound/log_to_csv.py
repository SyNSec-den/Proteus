import csv

column_name = 'issues_count'
log_data = [(1, 5L, -9.0, 0.198384831622735, -8.8, 2.3796790749778354),
            (2, 10L, -9.0, 0.10379160858796604, -9.0, 2.314434674458951),
            (3, 15L, -10.0, 0.1881653085525367, -9.2, 2.2842594659504813),
            (4, 20L, -10.0, 0.2213113193198547, -9.2, 1.7647010350614019),
            (5, 25L, -10.0, 0.08655818736733391, -9.2, 1.5051836808617511),
            (6, 30L, -10.0, 0.12540520898545407, -9.4, 1.40149463703155),
            (7, 35L, -10.0, 0.12154288575809202, -9.4, 1.5473831561050122),
            (8, 40L, -10.0, 0.08280008796010746, -9.4, 1.563758989170399),
            (9, 45L, -10.0, 0.11044359615464132, -9.4, 1.4005970553525795),
            (10, 50L, -10.0, 0.07966413685851961, -9.4, 1.5190235796214204),
            (11, 55L, -10.0, 0.08611410446355712, -9.4, 1.4194504821271534),
            (12, 60L, -10.0, 0.08376277658371688, -9.4, 1.4602536651590847),
            (13, 65L, -10.0, 0.0644784702829888, -9.4, 1.1554711025844067),
            (14, 70L, -10.0, 0.0705190785862602, -9.4, 1.1846847425979334),
            (15, 75L, -10.0, 0.06807939596760032, -9.4, 1.2445091948157074),
            (16, 80L, -10.0, 0.055352436990784654, -9.4, 1.349574194133837),
            (17, 85L, -10.0, 0.06068887530437946, -9.6, 1.1539203957178061),
            (18, 90L, -10.0, 0.04520143699934159, -9.6, 1.3396291717034114),
            (19, 95L, -10.0, 0.0368090741812241, -9.6, 1.2864620169013994),
            (20, 100L, -10.0, 0.055768794378364565, -9.6, 1.1366389403982762),
            (21, 105L, -10.0, 0.03190038245827167, -9.6, 1.203859073844187),
            (22, 110L, -10.0, 0.051221964793464476, -9.6, 1.161350847449445),
            (23, 115L, -10.0, 0.03943438046869376, -9.6, 1.2737995564506472),
            (24, 120L, -10.0, 0.03855719674244369, -9.6, 1.1360180575955967),
            (25, 125L, -10.0, 0.05309185616425705, -9.6, 1.1180838721661739)]

with open('cost_function_graph.csv', 'w') as csvfile:
    columns = ['X', column_name]
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    for entry in log_data:
        writer.writerow({
            'X': entry[0],
            column_name: entry[2]
        })
